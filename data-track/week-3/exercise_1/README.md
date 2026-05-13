# Exercise 1: Write a Retry Function

Make a fragile API fetch resilient to transient network failures.

## Setup

```bash
pip install -r requirements.txt
```

## The task

The starter `exercise.py` contains a `fetch_data(url)` that crashes on the first failure. Your job is to implement `fetch_data_retried` — the resilient version — using the TODO stubs in the file.

1. Add a `max_retries: int = 3` parameter.
2. Wrap the request in a `for attempt in range(max_retries):` loop.
3. Only retry on `requests.exceptions.ConnectionError` and `requests.exceptions.Timeout`. Let `HTTPError` (4xx/5xx) propagate immediately — those are permanent.
4. Between attempts, sleep `2 ** attempt` seconds (1s, 2s, 4s for the default 3 retries).
5. After the final failed attempt, re-raise the original exception.
6. Print `"Attempt {n} failed, retrying in {wait}s..."` before each sleep.

## Success criteria

- Calling `fetch_data_retried(<a working URL>)` returns a JSON dict on the first try.
- Calling `fetch_data_retried(<a URL that timeouts>)` prints two retry messages, then raises after the third attempt.
- A 404 raises immediately without retrying.

## Stretch

- Add a `backoff_base: float = 2.0` parameter so the caller can control the growth rate.
- Add jitter (`+ random.uniform(0, 1)` seconds) so a stampede of clients does not retry in lockstep.
