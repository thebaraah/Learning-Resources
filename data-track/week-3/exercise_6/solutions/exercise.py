"""Exercise 6 — Reference solution.

Read the `# WHY ...:` notes, not the code.
"""
from __future__ import annotations

import sqlite3
import time
from pathlib import Path

import requests
from pydantic import BaseModel, Field, ValidationError, field_validator


DB_PATH = Path(__file__).parent.parent / "weather.db"
# WHY parent.parent: solutions/ sits inside exercise_6/. The DB stays at
# exercise_6/weather.db so both starter and solution share the same file.


# --- from Exercise 4 -------------------------------------------------------
class WeatherReading(BaseModel):
    station: str = Field(min_length=1)
    temperature_c: float = Field(ge=-90, le=60)
    humidity_pct: int = Field(ge=0, le=100)
    timestamp: str

    @field_validator("station")
    @classmethod
    def normalize_station(cls, v: str) -> str:
        cleaned = v.strip()
        if not cleaned:
            raise ValueError("station cannot be blank")
        return cleaned.title()


def validate_batch(records: list[dict]) -> tuple[list[WeatherReading], list[dict]]:
    valid, errors = [], []
    for i, record in enumerate(records):
        try:
            valid.append(WeatherReading(**record))
        except ValidationError as e:
            errors.append({"index": i, "record": record, "errors": e.errors()})
    return valid, errors


# --- from Exercise 1 -------------------------------------------------------
def fetch_weather(latitude: float, longitude: float, days: int = 1, max_retries: int = 3) -> dict:
    """Fetch Open-Meteo hourly forecast with retries on transient errors."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m",
        "forecast_days": days,
    }
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


# --- step 2: normalize the columnar API response --------------------------
def normalize_open_meteo(api_response: dict, station: str) -> list[dict]:
    """Flatten Open-Meteo's {time:[], temperature_2m:[], ...} into row-dicts."""
    hourly = api_response["hourly"]
    # WHY zip(..., strict=True) over a range-loop: strict=True raises a clear
    # ValueError("zip() has arguments with different lengths") the moment the
    # columns mismatch, pointing directly at the schema problem. A bare
    # `for i in range(len(time))` would crash later with a less-informative
    # IndexError — or, worse, silently truncate to the shortest column if you
    # used plain zip() without strict=True.
    return [
        {
            "station": station,
            "timestamp": ts,
            "temperature_c": temp,
            "humidity_pct": hum,
        }
        for ts, temp, hum in zip(
            hourly["time"],
            hourly["temperature_2m"],
            hourly["relative_humidity_2m"],
            strict=True,
        )
    ]


# --- from Exercise 5 -------------------------------------------------------
def create_table(db_path: str) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS weather_readings (
                station TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                temperature_c REAL NOT NULL,
                humidity_pct INTEGER NOT NULL,
                UNIQUE(station, timestamp)
            )
            """
        )


def upsert_readings(db_path: str, readings: list[dict]) -> None:
    rows = [
        (r["station"], r["timestamp"], r["temperature_c"], r["humidity_pct"])
        for r in readings
    ]
    with sqlite3.connect(db_path) as conn:
        conn.executemany(
            """
            INSERT INTO weather_readings (station, timestamp, temperature_c, humidity_pct)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(station, timestamp) DO UPDATE SET
                temperature_c = excluded.temperature_c,
                humidity_pct = excluded.humidity_pct
            """,
            rows,
        )


def row_count(db_path: str) -> int:
    with sqlite3.connect(db_path) as conn:
        return conn.execute("SELECT COUNT(*) FROM weather_readings").fetchone()[0]


def main() -> None:
    raw = fetch_weather(latitude=55.67, longitude=12.56, days=1)
    records = normalize_open_meteo(raw, station="Copenhagen")
    print(f"Fetched: {len(records)} hourly records")

    valid, errors = validate_batch(records)
    print(f"Valid: {len(valid)}, Errors: {len(errors)}")

    create_table(str(DB_PATH))
    # WHY model_dump() not the Pydantic model itself: SQLite's executemany
    # takes tuples or sequences. .model_dump() converts the model back to
    # a plain dict the upsert helper already knows how to handle.
    upsert_readings(str(DB_PATH), [v.model_dump() for v in valid])
    print(f"Rows in DB: {row_count(str(DB_PATH))}")
    # WHY rerunning produces the same row count: UNIQUE(station, timestamp)
    # + ON CONFLICT DO UPDATE means the second run updates the 24 existing
    # rows instead of inserting another 24. That is idempotency in action.


if __name__ == "__main__":
    main()
