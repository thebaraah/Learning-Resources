"""Exercise 1: Write a Retry Function.

The function below crashes on the first failure. In production pipelines you
need it to survive transient network errors (server restarts, DNS blips,
rate-limit blocks) without giving up immediately.

Steps:
  1. Add a `max_retries` parameter with a default of 3.
  2. Wrap the request in a retry loop with exponential backoff
     (wait `2 ** attempt` seconds between attempts: 1s, 2s, 4s).
  3. Only retry on `requests.exceptions.ConnectionError` and
     `requests.exceptions.Timeout`. Other errors (4xx HTTPError) should
     fail immediately - they are permanent.
  4. After the final attempt, re-raise the original exception.
  5. Print a message before each retry:
     "Attempt {n} failed, retrying in {wait}s..."

Hint: use `for attempt in range(max_retries):` and `time.sleep(wait_time)`.
"""
import requests


# BAD: no retry, crashes immediately on the first transient failure
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
    raise NotImplementedError("Implement me using the TODOs above.")


if __name__ == "__main__":
    # Expected: prints "Got 24 timestamps" on success, or prints retry messages
    # then raises after max_retries failed attempts.
    data = fetch_data_retried("https://api.open-meteo.com/v1/forecast?latitude=55.67&longitude=12.56&hourly=temperature_2m&forecast_days=1")
    print(f"Got {len(data.get('hourly', {}).get('time', []))} timestamps")
