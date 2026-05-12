# Exercise 5: SQLite Writer

Persist validated weather data to SQLite, with idempotent upserts.

## Setup

Pure standard library — `sqlite3` ships with Python.

```bash
python3 exercise.py
```

## The task

1. `create_table(db_path)`: create `weather_readings` with `station TEXT`, `timestamp TEXT`, `temperature_c REAL`, `humidity_pct INTEGER`. Add `UNIQUE(station, timestamp)`. Wrap in `CREATE TABLE IF NOT EXISTS`.
2. `upsert_readings(db_path, readings)`: insert each row with parameterised SQL and `ON CONFLICT(station, timestamp) DO UPDATE SET temperature_c = excluded.temperature_c, humidity_pct = excluded.humidity_pct`.
3. `query_by_station(db_path, station) -> list[dict]`: parameterised `SELECT ... WHERE station = ?`. Use `conn.row_factory = sqlite3.Row` so each row converts via `dict(row)`.

## Success criteria

Running `python3 exercise.py` prints:

```text
After first insert: 1 Copenhagen reading(s)
After upsert: 1 Copenhagen reading(s)  temp_c=19.0
```

The second insert updates the existing row (idempotency). The temperature changes from 18.5 → 19.0 without duplicating the row.

## Stretch

- Add a `with sqlite3.connect(...) as conn:` context manager so the file is closed cleanly on exceptions.
- Add an `ingested_at` column with `DEFAULT CURRENT_TIMESTAMP` and update it on every upsert.
