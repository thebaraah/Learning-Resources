"""Exercise 2: Paginated API Fetch.

Write a function that fetches every page of a paginated endpoint and returns
the combined results.

Steps:
  1. Implement `fetch_all_pages(base_url: str) -> list[dict]`.
  2. Each page response has the shape:
       {"results": [...], "page": <int>, "total_pages": <int>}
  3. Loop until `page >= total_pages`, incrementing the `?page=N` query param.
  4. Collect all `results` into a single flat list.
  5. Sleep 0.5 seconds between requests so you do not hammer the server.

Hint: pass `params={"page": page}` to `requests.get()` so requests builds the
query string for you. Set `timeout=10`.

For testing, this stand-in serves a fake 3-page paginator over Open-Meteo
data. Run the file as `python exercise.py` to see your implementation in
action against a local stub — no remote pagination needed.
"""
from __future__ import annotations

import requests


# TODO 1: implement fetch_all_pages
def fetch_all_pages(base_url: str) -> list[dict]:
    """Fetch every page of a paginated API and return one flat list."""
    raise NotImplementedError("Implement me. See the steps in the module docstring.")


# --- Local stub so you can verify without a real paginated API -------------
# This pretends to be a 3-page paginator. Your fetch_all_pages should call
# `simulate_paginated_request(page=N)` and assemble all results.

def simulate_paginated_request(page: int) -> dict:
    """Stand-in for `requests.get(...).json()` against a paginated endpoint."""
    total_pages = 3
    page_size = 4
    start = (page - 1) * page_size
    return {
        "page": page,
        "total_pages": total_pages,
        "results": [{"id": start + i, "value": f"item_{start + i}"} for i in range(page_size)],
    }


if __name__ == "__main__":
    # If your fetch_all_pages is implemented, swap the stub call in.
    # For now, run the stub directly to verify the contract you must satisfy:
    for p in range(1, 4):
        response = simulate_paginated_request(p)
        print(f"page {response['page']} of {response['total_pages']}: {len(response['results'])} items")

    # Expected after refactor:
    #   `fetch_all_pages(...)` returns a flat list of 12 dicts
    #   (3 pages × 4 items per page).
