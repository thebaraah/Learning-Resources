"""Exercise 1 — Reference solution.

Read the `# WHY ...:` notes, not the code. The reasoning is the teaching content.
"""
import time

import requests


# BAD: no retry, crashes immediately on the first transient failure
# (kept for contrast — see fetch_data_retried below for the answer)
def fetch_data(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


# TODO 1: add a `max_retries: int = 3` parameter
# TODO 2: wrap the request in a `for attempt in range(max_retries):` loop
# TODO 3: catch only ConnectionError + Timeout, not HTTPError
# TODO 4: on the final attempt, re-raise instead of swallowing
# TODO 5: print "Attempt {n} failed, retrying in {wait}s..." before each sleep
def fetch_data_retried(url: str, max_retries: int = 3) -> dict:
    # WHY default 3: small enough to fail fast in dev, large enough to ride out
    # a multi-second server hiccup. Production teams often go to 5 with longer
    # base sleeps; 3 is fine for a first pass.
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            # WHY catch these two only: ConnectionError + Timeout are *transient*
            # (network blip, server restart). HTTPError covers 4xx/5xx, which
            # for 4xx are permanent (bad URL, bad credentials) and we do not
            # want to mask them by retrying.
            if attempt == max_retries - 1:
                # WHY re-raise on the last attempt: the caller needs to know
                # the operation failed. Swallowing the exception and returning
                # `{}` or `None` would hide the failure and let bad downstream
                # logic execute on empty data.
                raise
            wait_time = 2 ** attempt
            # WHY exponential backoff: a constant 1s retry hammers a struggling
            # server. 1s, 2s, 4s gives the server time to recover.
            print(f"Attempt {attempt + 1} failed ({type(e).__name__}), retrying in {wait_time}s...")
            time.sleep(wait_time)
    # WHY unreachable but kept: makes the type-checker happy (the loop either
    # returns or raises before reaching here).
    raise RuntimeError("unreachable")


if __name__ == "__main__":
    # Expected: prints "Got 24 timestamps" (24 hourly entries for one forecast day)
    data = fetch_data_retried(
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=55.67&longitude=12.56&hourly=temperature_2m&forecast_days=1"
    )
    print(f"Got {len(data.get('hourly', {}).get('time', []))} timestamps")
