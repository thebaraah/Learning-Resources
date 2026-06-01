# Exercise 5: CI Smoke Test

Wire a GitHub Actions workflow that runs pytest on every push, then confirm CI catches a broken test.

## Setup

You need a GitHub repository for this exercise. Use your Week 5 assignment repo or create a new one. Copy these files from this exercise into the same paths in your repo:

- `.github/workflows/ci.yml`
- `tests/test_smoke.py`

## Task

1. Open `.github/workflows/ci.yml` and fill in the three TODOs.
2. Push to GitHub and confirm the Actions tab shows a green run.
3. Change `assert True` to `assert False` in `tests/test_smoke.py` and push. Confirm CI fails.
4. Revert the change and push again. Confirm CI goes green.
5. Open a pull request and confirm the same workflow runs for `pull_request` events.

## Success criteria

- CI runs on every push to `main` and on every pull request.
- A broken test causes the CI job to fail.
- A passing test causes the CI job to succeed.
- You can read the test output in the Actions tab.

## Stretch

- Add a `ruff check .` step before the test step.
- Update the install step so CI installs both tools (for example: `pip install pytest ruff`).
- Break it by writing a line of code that ruff flags (e.g. an unused import). Confirm CI fails on lint, not on tests.
- Why should you run lint before tests? (Hint: think about which check is cheaper.)
