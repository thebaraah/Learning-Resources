"""Exercise 6: Mini Pipeline.

Combine everything from exercises 1-5 into a single end-to-end ingestion
script: fetch weather data from the Open-Meteo API, validate with Pydantic,
upsert into SQLite. Re-running the script must not duplicate rows
(idempotency).

Steps:
  1. Implement `fetch_weather(latitude, longitude, days=1)` using `requests`
     with a `timeout=10` and the retry pattern from Exercise 1.
  2. Implement `normalize_open_meteo(api_response) -> list[dict]` that
     flattens Open-Meteo's columnar response into one record per hour with
     keys: station, timestamp, temperature_c, humidity_pct.
  3. Reuse the `WeatherReading` model and `validate_batch` function from
     Exercise 4.
  4. Reuse `create_table` + `upsert_readings` from Exercise 5.
  5. Run the pipeline twice and confirm the row count does not double.

Hint: Open-Meteo returns
  {"hourly": {"time": [...], "temperature_2m": [...], "relative_humidity_2m": [...]}}
where time[i], temperature_2m[i], and relative_humidity_2m[i] all line up.

The file `weather.db` is gitignored.
"""
from __future__ import annotations

# TODO: import requests, time, sqlite3, the Pydantic bits, and the helpers
# from earlier exercises (you can copy them in, or factor them out).


# TODO 1: fetch_weather with retry
def fetch_weather(latitude: float, longitude: float, days: int = 1) -> dict:
    """Fetch hourly weather forecast from Open-Meteo. Retry on transient errors."""
    raise NotImplementedError


# TODO 2: normalize the columnar Open-Meteo response into row-dicts
def normalize_open_meteo(api_response: dict, station: str) -> list[dict]:
    """Convert {time: [...], temperature_2m: [...], ...} into a list of dicts."""
    raise NotImplementedError


# TODO 3: bring in WeatherReading + validate_batch (or import from exercise_4)
# TODO 4: bring in create_table + upsert_readings (or import from exercise_5)


def main() -> None:
    raw = fetch_weather(latitude=55.67, longitude=12.56, days=1)
    records = normalize_open_meteo(raw, station="Copenhagen")
    print(f"Fetched: {len(records)} hourly records")

    # valid, errors = validate_batch(records)
    # print(f"Valid: {len(valid)}, Errors: {len(errors)}")

    # create_table("weather.db")
    # upsert_readings("weather.db", [v.model_dump() for v in valid])
    # print(f"Rows in DB: {row_count('weather.db')}")

    # Expected on the first run:
    #   Fetched: 24 hourly records
    #   Valid: 24, Errors: 0
    #   Rows in DB: 24
    # Expected on the second run (same script):
    #   Fetched: 24 hourly records
    #   Valid: 24, Errors: 0
    #   Rows in DB: 24   # UNCHANGED — upsert, not append


if __name__ == "__main__":
    main()
