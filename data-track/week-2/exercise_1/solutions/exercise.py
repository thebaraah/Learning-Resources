"""Reference solution (in-place over the starter).

The original `# TODO 1` comment is preserved next to the answer so the
question and answer read together.
"""
# TODO 1: import the config module you create in step 2 instead of
# defining API_KEY and BASE_URL inline above.
# Example: from config import API_KEY, BASE_URL
# WHY centralised config: every other file in this exercise can do
# `from config import API_KEY` and get the same values. The .env file
# is the single source of truth, and config.py is the single read-point.
from config import API_KEY, BASE_URL


def fetch_data() -> str:
    """Pretend to call an API. We just return a string here so the
    exercise stays runnable without network access."""
    return f"GET {BASE_URL}/data with key={API_KEY[:6]}..."


# Expected: 'GET https://api.example.com/data with key=sk-abc...'
# (After refactor, the same line, but with the values from your .env.)
print(fetch_data())
