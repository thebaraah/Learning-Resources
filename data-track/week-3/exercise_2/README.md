# Exercise 2: Paginated API Fetch

Implement a loop that collects every page of a paginated API into one list.

## Setup

```bash
pip install -r requirements.txt
```

## The task

The starter `exercise.py` ships a `simulate_paginated_request(page)` stub that pretends to be a 3-page paginator. Your job is to implement `fetch_all_pages(base_url)` that:

1. Loops over pages starting at `page=1`.
2. Sends each request with `params={"page": page}` (and `timeout=10`).
3. Collects each page's `results` into a single flat list.
4. Stops when `page >= total_pages`.
5. Sleeps 0.5s between requests with `time.sleep(0.5)`.

You may verify against the local stub first by calling `simulate_paginated_request` directly. When wiring up to a real API, swap in `requests.get(base_url, params={"page": page}, timeout=10).json()`.

## Success criteria

- `fetch_all_pages(...)` returns a list of 12 dicts when using the local stub (3 pages × 4 items per page).
- The function does not request additional pages once `page == total_pages`.
- A 0.5s delay sits between successive requests.

## Stretch

- Add a `max_pages` safety cap so a buggy API that always reports `total_pages: 999` cannot run forever.
- Support cursor-based pagination (the response carries `next_cursor` instead of `total_pages`).
