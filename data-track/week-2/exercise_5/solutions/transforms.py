"""Reference solution: pure transforms for Exercise 5.

Each function:
  - takes data in, returns NEW data out (no mutation)
  - has no I/O (no file system, no network)
  - is testable with a hand-rolled list of dicts
"""


def filter_active_adults(users: list[dict]) -> list[dict]:
    """Keep only users with status='active' AND age >= 18."""
    return [u for u in users if u.get("status") == "active" and u.get("age", 0) >= 18]


# WHY return a new dict instead of mutating: the caller's `user` dict
# is left intact. If anything downstream still needs the original
# email format (audit log, original-vs-cleaned diff), it's still there.
def clean_email(user: dict) -> dict:
    return {**user, "email": user["email"].lower().strip()}


# WHY apply clean_email here as a list comprehension instead of inside
# filter_active_adults: each transform does ONE thing. Composition at
# the orchestrator (main.py) glues them; the units stay testable.
def clean_emails(users: list[dict]) -> list[dict]:
    return [clean_email(u) for u in users]
