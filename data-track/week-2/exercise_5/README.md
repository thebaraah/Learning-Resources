# Week 2 — Exercise 5: Refactor a "god function" (capstone)

**Concepts:** all of Week 2 — config & secrets, dataclasses, separation of concerns, composable transforms, pytest, AI-assisted refactoring.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Your task

Read `exercise.py` and run it once with `python exercise.py` to see the BAD baseline. Then rebuild it as a clean pipeline:

1. **Data model** — a `User` dataclass in `models.py` with fields `name`, `email`, `age`, `status`.
2. **Configuration** — paths in `.env`, loaded via a `config.py` module that exposes `INPUT_PATH` and `OUTPUT_PATH`.
3. **Layers**:
   - `read_users(path) -> list[dict]` (I/O)
   - `filter_active_adults(users) -> list[dict]` (pure)
   - `clean_email(user) -> dict` (pure, returns a new dict — don't mutate)
   - `save_users(users, path) -> None` (I/O)
4. **Orchestrator** — `main.py` that wires them together. Convert cleaned dicts to `User` instances before serialising back via `dataclasses.asdict`.
5. **Tests** — at least 3 pytest tests for the pure functions in `tests/test_transforms.py`.
6. **AI reflection** — `AI_NOTES.md` with two short paragraphs:
   - One helpful suggestion an LLM gave you and what it actually caught.
   - One suggestion you rejected and why.

## Success criteria

- `python main.py` prints `Processed 3 users` and writes `active_users.json` containing Alice, Dan, and Eve with lowercased + stripped emails.
- `pytest tests/` shows all green.
- The original `users.json` is unchanged after the run (proof your transforms didn't mutate the input).

## Suggested file layout

```text
exercise_5/
├── .env                       # gitignored
├── .env.example               # committed
├── users.json                 # input (provided)
├── active_users.json          # output (generated)
├── config.py
├── models.py
├── transforms.py
├── io_layer.py                # NOT named io.py (shadows stdlib!)
├── main.py
├── AI_NOTES.md
├── requirements.txt
└── tests/
    └── test_transforms.py
```

## Stretch

Add a `--dry-run` flag to `main.py` (using `argparse`) that runs the pipeline but skips the `save_users` step. Useful for confirming a pipeline change won't corrupt your output before you commit to running it.
