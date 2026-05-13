"""Exercise 2 — Reference solution.

Read the `# WHY ...:` notes, not the code.
"""
from __future__ import annotations

import time


# TODO 1: implement fetch_all_pages
def fetch_all_pages(base_url: str, fetcher=None) -> list[dict]:
    """Fetch every page of a paginated API and return one flat list.

    `fetcher` is the callable that returns a page (a dict with results +
    page + total_pages). The default is `_request_page` which calls
    `requests.get(base_url, params=..., timeout=10).json()`.
    """
    # WHY pass `fetcher` in: in production this would be a `requests.get(...)`
    # call. For the local stub-driven test, we inject `simulate_paginated_request`
    # so the solution runs offline. Dependency injection is the same pattern
    # you saw in Week 2's separation-of-concerns chapter.
    if fetcher is None:
        fetcher = lambda page: _request_page(base_url, page)  # noqa: E731

    all_results: list[dict] = []
    page = 1

    while True:
        data = fetcher(page)
        # WHY .extend() not .append(): each page's `results` is itself a list.
        # .append([...]) would give a list-of-lists; .extend([...]) flattens.
        all_results.extend(data["results"])

        # WHY check >= total_pages, not `page < total_pages`: once we've
        # processed `total_pages`, we're done. Off-by-one bugs hide here.
        if page >= data["total_pages"]:
            break

        page += 1
        # WHY 0.5s delay: APIs publish a rate limit (e.g. 60 req/min). A short
        # delay keeps you well under the limit and is invisible to users.
        # Use `time.sleep(delay)` after a successful page, not before — there
        # is no need to wait before the very first request.
        time.sleep(0.5)

    return all_results


def _request_page(base_url: str, page: int) -> dict:
    """Real HTTP call for production use."""
    import requests
    response = requests.get(base_url, params={"page": page}, timeout=10)
    response.raise_for_status()
    return response.json()


# --- Local stub so you can verify without a real paginated API -------------

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
    # Expected: 12 items collected across 3 pages.
    results = fetch_all_pages("unused", fetcher=simulate_paginated_request)
    print(f"Collected {len(results)} items across all pages")
    print(f"First: {results[0]}, last: {results[-1]}")
