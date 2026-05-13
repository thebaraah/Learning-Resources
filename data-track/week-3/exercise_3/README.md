# Exercise 3: Read and Normalize File Formats

Read weather data from two different formats with different field names, normalize both into a single pipeline shape.

## Setup

Pure standard library — no `pip install` needed.

```bash
python3 exercise.py
```

## The task

The `data/` folder ships two files:

- `stations.csv`: 3 rows with columns `station_name`, `temp`, `humidity`, `date`
- `readings.json`: 2 rows with keys `station`, `temperature_c`, `humidity_pct`, `timestamp`

Note how the two sources disagree on **every** field name. Your job is to converge them.

1. Implement `read_csv_file(path) -> list[dict]` using `csv.DictReader`.
2. Implement `read_json_file(path) -> list[dict]` using `json.load`.
3. Implement `normalize_record(record) -> dict` that produces the canonical shape:
   ```python
   {"station": str, "temperature_c": float, "humidity_pct": int, "timestamp": str}
   ```
   regardless of the input field names. Hint: chained `.get()` calls with fallbacks.

## Success criteria

Running the script prints 5 rows, each with exactly the four canonical keys. Both formats round-trip cleanly. Print order: CSV rows first, then JSON rows.

## Stretch

- Handle the case where `temp` is missing entirely (default to `None`, not a crash).
- Add a `normalize_records(records: list[dict]) -> list[dict]` helper that maps over a list.
