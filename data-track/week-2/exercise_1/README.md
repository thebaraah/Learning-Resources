# Week 2 — Exercise 1: Move Secrets to .env

**Concepts:** environment variables, `python-dotenv`, centralised `config.py` module.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

Your `.env` is gitignored (the repo's `.gitignore` covers it). `.env.example` stays committed and documents the expected variable names without leaking real values.

## Your task

1. Read the existing `exercise.py`. Notice the hardcoded `API_KEY` and `BASE_URL`.
2. Create a `config.py` next to `exercise.py`. Import `os` and `dotenv.load_dotenv`. Call `load_dotenv()` at module top, then expose `API_KEY` and `BASE_URL` as module-level variables read from `os.environ`.
3. Refactor `exercise.py`: remove the inline `API_KEY = "..."` and `BASE_URL = "..."` lines, and replace them with `from config import API_KEY, BASE_URL`.
4. Run `python exercise.py`. The output should be the same as before, but no secrets appear in the .py files.

## Success criteria

- `git diff exercise.py` shows the inline secrets removed and replaced by a `from config import ...` line.
- Deleting `.env` and re-running raises an obvious error (no secret silently slips through as `None`).

## Stretch

Make `config.py` raise `ValueError("API_KEY is required")` if the variable is missing, instead of letting `None` propagate.
