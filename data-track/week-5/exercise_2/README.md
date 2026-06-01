# Exercise 2: Cache-Friendly Dockerfile

Reorder a Dockerfile so that `pip install` is cached separately from source code changes.

## Setup

No extra setup — `src/pipeline.py` uses only `os` from the standard library. `requests` and `pandas` are in `requirements.txt` but not imported yet; they represent real project dependencies, and `pandas` is intentionally heavier so reinstall timing differences are easier to notice.

## Task

1. Build the image as-is and note how long the install step takes:
   ```bash
   docker build -t pipeline-practice:2.0 .
   ```
2. Add a blank line to `src/pipeline.py` and build again. Observe that `pip install` runs again from scratch (this should be noticeably slower because of the heavier dependency set).
3. Open `Dockerfile` and fix the `TODO 1`: reorder the `COPY` and `RUN` instructions so dependency installs are cached.
4. Build again after the fix, then add another blank line to `src/pipeline.py` and build a fourth time. Confirm that `pip install` is now served from cache (`---> Using cache`).

## Success criteria

- After fixing the Dockerfile, editing `src/pipeline.py` does **not** trigger a pip reinstall.
- `docker build` output shows `---> Using cache` for the pip install layer after a code-only change.

## Stretch

- Add a second package to `requirements.txt` (e.g. `pydantic==2.6.1`) and rebuild. Is the install layer invalidated? Why?
- Demonstrate build context vs image contents with `.dockerignore`:
   1. Create a `.dockerignore` file containing `requirements.txt`.
   2. Run `docker build --no-cache -t pipeline-practice:2.0 .` and observe the failure.
   3. Remove `requirements.txt` from `.dockerignore`.
   4. Build again and confirm it succeeds.
   5. Explain why: Docker `COPY` reads from the current build context, not from files that existed in a previously built image.
