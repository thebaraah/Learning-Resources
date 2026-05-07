# Week 1 — Exercise 6: The Pipeline CLI

**Concepts:** CLI arguments via [`argparse`](https://docs.python.org/3/library/argparse.html) (Ch6), [logging levels](https://docs.python.org/3/howto/logging.html) (Ch8), `pathlib` (Ch9).

You are given a tiny CSV cleaner (`exercise_6.py`) that mostly works, but it has three problems any production pipeline would fix on day one:

1. The input and output paths are **hard-coded**. A teammate can't reuse it on a different file.
2. It always logs at `INFO`. You can't quiet it for a clean run, or crank it up to `DEBUG` when something looks off.
3. Every message uses `logging.info()` regardless of what it actually is. Skipped rows should warn; per-row trace should be DEBUG; the summary is INFO.

Your task: wrap the cleaner with a proper CLI.

## Goal

Make the script runnable like this:

```bash
python exercise_6.py --input data/messy_users.csv --output cleaned.json --log-level DEBUG
```

`--log-level` should accept `DEBUG`, `INFO`, `WARNING`, or `ERROR` (default `INFO`).

## Steps

1. **Add `argparse`** at the top of `main()`:
   - `--input <path>` (required)
   - `--output <path>` (required)
   - `--log-level <name>` (optional, default `INFO`, choices: `DEBUG INFO WARNING ERROR`)
2. **Configure the root logger** to use the chosen level. Hint: `logging.basicConfig(level=getattr(logging, args.log_level))`.
3. **Replace the wrong `logging.info()` calls** in `clean_rows()` with the right level (look for the `# FIXME` comments).
4. **Wire the input/output paths** from `args` into the `csv.reader` / `json.dump` calls in `main()`.

## What "right" looks like

Run with `--log-level WARNING` against the sample data: you should see **only** the two `WARNING` lines about the skipped rows, no DEBUG, no INFO.

Run with `--log-level DEBUG`: you should see one DEBUG line per row processed, two WARNING lines for the skipped rows, and one INFO summary at the end.

The output JSON file should contain only the two valid rows (ids 1 and 3) with their emails lowercased and names trimmed.

## Sample data

`data/messy_users.csv` (already in this branch):

```csv
id,name,email
1,  Alice  ,Alice@example.com
2,  ,bob@example.com
3,Carol,CAROL@EXAMPLE.COM
4,,david@example.com
```

Rows 2 and 4 have empty names and should be skipped with a `WARNING`.

## When you're stuck

- The `argparse` chapter ([Ch6](https://www.notion.so/hackyourfuture/Command-Line-Interface-Habits-c1adcf93d6e845479c7efa3a1afb60f6)) shows the same `add_argument(...)` shape.
- The `logging` chapter ([Ch8](https://www.notion.so/hackyourfuture/Logging-in-Python-cc769ff601b74fa18f7fb3447883b9d6)) lists the five levels and what each is for.
- Picking the right level is the harder skill: when in doubt, ask "would I want to see this when the pipeline is running clean?" If yes → `INFO`. If only when something needs attention → `WARNING`. If only when I'm hunting a bug → `DEBUG`.
