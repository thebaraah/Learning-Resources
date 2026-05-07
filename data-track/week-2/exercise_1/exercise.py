"""Exercise 1: Move Secrets to .env.

The script below has hardcoded credentials. Refactor it so that nothing
sensitive lives in the .py files.

Steps:
  1. Create a .env file (NOT committed) with API_KEY and BASE_URL.
  2. Create a config.py module that loads them via python-dotenv.
  3. Refactor THIS file to import API_KEY and BASE_URL from config.
  4. Add `.env` to .gitignore (already done in this repo).

A starter `.env.example` is included next to this file. Copy it to `.env`
and fill in real-looking values, then refactor the code.
"""
# BAD: secrets in code
API_KEY = "sk-abc123-secret"
BASE_URL = "https://api.example.com"

# TODO 1: import the config module you create in step 2 instead of
# defining API_KEY and BASE_URL inline above.
# Example: from config import API_KEY, BASE_URL


def fetch_data() -> str:
    """Pretend to call an API. We just return a string here so the
    exercise stays runnable without network access."""
    return f"GET {BASE_URL}/data with key={API_KEY[:6]}..."


# Expected: 'GET https://api.example.com/data with key=sk-abc...'
# (After refactor, the same line, but with the values from your .env.)
print(fetch_data())
