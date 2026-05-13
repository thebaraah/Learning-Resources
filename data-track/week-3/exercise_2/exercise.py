"""Exercise 2: Paginated API Fetch.

Write a function that fetches every page of a paginated endpoint and returns
the combined results.

Steps:
  1. Implement `fetch_all_pages(base_url: str, fetcher=None) -> list[dict]`.
  2. Each page response has the shape:
       {"results": [...], "page": <int>, "total_pages": <int>}
  3. Call `fetcher(page)` to get each page. When `fetcher` is None, default to
     calling `simulate_paginated_request(page)` (or a real HTTP request for
     production use).
  4. Loop until `page >= total_pages`, incrementing the page counter each pass.
  5. Collect all `results` into a single flat list.
  6. Sleep 0.5 seconds between requests so you do not hammer the server.

Hint: `fetcher` is a callable that takes a page number and returns a dict.
Passing it in makes the function testable without a real server.

For testing, run `python exercise.py` — the stub below serves a fake 3-page
paginator so you can verify your implementation offline.
"""
from __future__ import annotations


# TODO 1: implement fetch_all_pages
def fetch_all_pages(base_url: str, fetcher=None) -> list[dict]:
    """Fetch every page of a paginated API and return one flat list.

    fetcher: callable(page: int) -> dict. Defaults to simulate_paginated_request
    for local testing; swap in a real HTTP caller for production.
    """
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
