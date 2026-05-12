# Exercise 6: Mini Pipeline

Combine exercises 1-5 into a single end-to-end ingestion: fetch → normalize → validate → store. Verify idempotency by running it twice.

## Setup

```bash
pip install -r requirements.txt
```

## The task

Build a pipeline that:

1. Fetches hourly weather from Open-Meteo for Copenhagen (`latitude=55.67, longitude=12.56`) using `requests` + retry logic from Exercise 1.
2. Normalizes the columnar API response into one record per hour with keys `station, timestamp, temperature_c, humidity_pct`. The API returns `{"hourly": {"time": [...], "temperature_2m": [...], "relative_humidity_2m": [...]}}` — all lists are aligned by index.
3. Validates each record with the `WeatherReading` model from Exercise 4 using `validate_batch`.
4. Upserts the valid records into a SQLite database `weather.db` using `create_table` + `upsert_readings` from Exercise 5.
5. Prints a summary: total fetched, valid, errors, rows in DB.

You may either copy the helpers from earlier exercises into this file, or import them (whichever feels cleaner).

## Success criteria

First run prints something like:

```text
Fetched: 24 hourly records
Valid: 24, Errors: 0
Rows in DB: 24
```

Second run (same script, same day) prints the **same** row count:

```text
Fetched: 24 hourly records
Valid: 24, Errors: 0
Rows in DB: 24   # idempotent — upsert did not duplicate
```

That same-row-count-on-rerun is the whole point of the upsert pattern.

## Stretch

- Run the pipeline for three cities in a loop, all writing to the same DB.
- Add a `raw_open_meteo` table (the raw JSON pattern from Ch6) and store the API response there before normalization.
- Wire in `logging.getLogger(__name__)` from Week 1 instead of `print()`.
