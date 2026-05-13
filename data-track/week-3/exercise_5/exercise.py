"""Exercise 5: SQLite Writer.

Store validated weather data in a SQLite database. Make the writer idempotent
so running the pipeline twice produces the same database state.

Steps:
  1. Implement `create_table(db_path)` that creates a `weather_readings`
     table with columns: station TEXT, timestamp TEXT, temperature_c REAL,
     humidity_pct INTEGER. Add a UNIQUE(station, timestamp) constraint.
  2. Implement `upsert_readings(db_path, readings)` that inserts rows with
     `ON CONFLICT(station, timestamp) DO UPDATE SET temperature_c=excluded...
     humidity_pct=excluded...`.
  3. Implement `query_by_station(db_path, station) -> list[dict]` that
     returns every reading for that station as dicts.
  4. Use parameterized queries (`?` placeholders) for every SQL operation.

Hint: `sqlite3.connect(db_path)` opens or creates the file. Use
`conn.row_factory = sqlite3.Row` so cursors yield dict-like rows that
`dict(row)` converts to a regular dict.

The file `weather.db` will be created next to this script and is gitignored.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / "weather.db"


# TODO 1: implement create_table
def create_table(db_path: str) -> None:
    """Create weather_readings if it does not exist."""
    raise NotImplementedError


# TODO 2: implement upsert_readings
def upsert_readings(db_path: str, readings: list[dict]) -> None:
    """Upsert a batch using ON CONFLICT(station, timestamp) DO UPDATE."""
    raise NotImplementedError


# TODO 3: implement query_by_station
def query_by_station(db_path: str, station: str) -> list[dict]:
    """Return every reading for the given station as a list of dicts."""
    raise NotImplementedError


if __name__ == "__main__":
    # Clean state for repeatable runs
    if DB_PATH.exists():
        DB_PATH.unlink()

    create_table(str(DB_PATH))

    initial = [
        {"station": "Copenhagen", "timestamp": "2025-01-15T10:00", "temperature_c": 18.5, "humidity_pct": 72},
        {"station": "Aarhus", "timestamp": "2025-01-15T10:00", "temperature_c": 15.2, "humidity_pct": 65},
        {"station": "Odense", "timestamp": "2025-01-15T10:00", "temperature_c": 16.1, "humidity_pct": 70},
    ]
    upsert_readings(str(DB_PATH), initial)
    print(f"After first insert: {len(query_by_station(str(DB_PATH), 'Copenhagen'))} Copenhagen reading(s)")

    # Re-insert with updated temperatures: should UPDATE, not duplicate
    updated = [
        {"station": "Copenhagen", "timestamp": "2025-01-15T10:00", "temperature_c": 19.0, "humidity_pct": 73},
        {"station": "Aarhus", "timestamp": "2025-01-15T10:00", "temperature_c": 15.5, "humidity_pct": 66},
        {"station": "Odense", "timestamp": "2025-01-15T10:00", "temperature_c": 16.4, "humidity_pct": 71},
    ]
    upsert_readings(str(DB_PATH), updated)

    cph = query_by_station(str(DB_PATH), "Copenhagen")
    print(f"After upsert: {len(cph)} Copenhagen reading(s)  temp_c={cph[0]['temperature_c']}")

    # Expected:
    #   After first insert: 1 Copenhagen reading(s)
    #   After upsert: 1 Copenhagen reading(s)  temp_c=19.0
