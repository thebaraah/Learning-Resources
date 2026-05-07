"""Reference solution: tests for the pure transforms in Exercise 5."""
import sys
from pathlib import Path

# WHY this sys.path tweak: the tests live in tests/ and import from the
# parent directory. Adding the parent to sys.path lets `import transforms`
# resolve when pytest runs from the exercise_5 root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from transforms import clean_email, clean_emails, filter_active_adults


@pytest.fixture
def sample_users() -> list[dict]:
    return [
        {"name": "Alice", "email": " ALICE@example.com ", "age": 30, "status": "active"},
        {"name": "Bob",   "email": "bob@example.com",     "age": 17, "status": "active"},
        {"name": "Carol", "email": "carol@example.com",   "age": 42, "status": "inactive"},
        {"name": "Dan",   "email": " DAN@example.com",    "age": 25, "status": "active"},
    ]


def test_filter_active_adults_keeps_only_adults_with_active_status(sample_users):
    result = filter_active_adults(sample_users)
    names = sorted(u["name"] for u in result)
    # Bob: minor (17). Carol: inactive. Alice + Dan survive.
    assert names == ["Alice", "Dan"]


def test_clean_email_returns_new_dict_does_not_mutate(sample_users):
    original = sample_users[0].copy()
    cleaned = clean_email(sample_users[0])
    assert cleaned["email"] == "alice@example.com"
    # WHY assert original unchanged: this is the silent mutation trap.
    # If clean_email modifies its input, the next caller sees the
    # cleaned version and the audit log of the original is lost.
    assert sample_users[0] == original


@pytest.mark.parametrize(
    "raw, expected",
    [
        (" UPPER@x.com ",  "upper@x.com"),
        ("noformat@x.com", "noformat@x.com"),
        ("MixedCase@X.COM", "mixedcase@x.com"),
    ],
)
def test_clean_email_normalisation_cases(raw, expected):
    user = {"name": "Test", "email": raw, "age": 30, "status": "active"}
    assert clean_email(user)["email"] == expected


def test_clean_emails_processes_full_list(sample_users):
    cleaned = clean_emails(sample_users)
    assert all(u["email"] == u["email"].lower().strip() for u in cleaned)
    # And the original still has the messy emails
    assert sample_users[0]["email"] == " ALICE@example.com "
