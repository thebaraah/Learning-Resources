# Week 2 — Exercise 3: Separate I/O from Logic

**Concepts:** thin I/O layer, pure functions, dependency injection, orchestrator.

## Setup

No extra packages — standard library only.

```bash
python exercise.py
```

## Your task

The god function `process_sales()` in `exercise.py` does three jobs at once: reads `sales.csv`, computes revenue with business rules baked in, and writes a report. Split it into four named functions:

1. `read_sales(path) -> list[dict]` — opens the CSV with `csv.DictReader` and returns the rows. No filtering, no arithmetic.
2. `calculate_revenue(rows) -> float` — pure function. Walks the list, skips rows where `price <= 0` or `quantity <= 0`, sums `price * quantity` for the rest. **Must not touch the filesystem.** You should be able to call it with a hand-rolled list of dicts and get the right number out.
3. `write_report(total, path) -> None` — writes the formatted line `"Total revenue: €{total:.2f}"` to disk.
4. `run_pipeline(input_path, output_path) -> None` — orchestrator: calls `read_sales`, `calculate_revenue`, `write_report` in that order.

## Success criteria

- `python exercise.py` produces `report.txt` containing `Total revenue: €125.97`.
- `calculate_revenue([{"price": "10", "quantity": "2"}])` returns `20.0` with **no file on disk** — the function works on data in memory.

## Stretch

Add a third I/O function `read_sales_from_url(url)` that fetches the same CSV from a URL. Notice that you don't need to change `calculate_revenue` at all — that's the payoff of separation.
