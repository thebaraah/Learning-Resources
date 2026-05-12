"""Exercise 5 — Reference solution.

Read the `# WHY ...:` notes, not the code.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent.parent / "weather.db"
# WHY parent.parent: solutions/ sits inside exercise_5/. The DB file lives
# at exercise_5/weather.db so both the starter and solution share it.


# TODO 1: implement create_table
def create_table(db_path: str) -> None:
    """Create weather_readings if it does not exist."""
    # WHY CREATE TABLE IF NOT EXISTS: this lets the function be safely called
    # at the start of every pipeline run without an explicit "did we already
    # create it?" check. Idempotency at the schema layer.
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
    # WHY no explicit conn.commit() / conn.close(): the `with` block does
    # both. It commits on a clean exit, rolls back on an exception, and
    # closes the connection either way.


# TODO 2: implement upsert_readings
def upsert_readings(db_path: str, readings: list[dict]) -> None:
    """Upsert a batch using ON CONFLICT(station, timestamp) DO UPDATE."""
    rows = [
        (r["station"], r["timestamp"], r["temperature_c"], r["humidity_pct"])
        for r in readings
    ]
    # WHY executemany over a loop of execute(): executemany batches the rows
    # into a single round-trip to the SQLite engine. For 1,000 rows the
    # difference is ~10x in wall-clock time.
    # WHY `excluded.<col>`: in an upsert, `excluded` refers to the row that
    # *would have been inserted*. The DO UPDATE branch reads from `excluded`
    # because the conflicting existing row is on the other side of the comma.
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


# TODO 3: implement query_by_station
def query_by_station(db_path: str, station: str) -> list[dict]:
    """Return every reading for the given station as a list of dicts."""
    with sqlite3.connect(db_path) as conn:
        # WHY row_factory = sqlite3.Row: by default a cursor yields tuples,
        # which forces the caller to remember column order. Row objects are
        # dict-like, and `dict(row)` produces a plain dict with the column
        # names as keys.
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(
            # WHY parameterised `?`: never f-string user input into SQL. A
            # station name of `'; DROP TABLE weather_readings; --` would
            # delete the table. The driver escapes the value for us.
            "SELECT * FROM weather_readings WHERE station = ?",
            (station,),
        )
        return [dict(row) for row in cursor.fetchall()]


if __name__ == "__main__":
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

    updated = [
        {"station": "Copenhagen", "timestamp": "2025-01-15T10:00", "temperature_c": 19.0, "humidity_pct": 73},
        {"station": "Aarhus", "timestamp": "2025-01-15T10:00", "temperature_c": 15.5, "humidity_pct": 66},
        {"station": "Odense", "timestamp": "2025-01-15T10:00", "temperature_c": 16.4, "humidity_pct": 71},
    ]
    upsert_readings(str(DB_PATH), updated)

    cph = query_by_station(str(DB_PATH), "Copenhagen")
    print(f"After upsert: {len(cph)} Copenhagen reading(s)  temp_c={cph[0]['temperature_c']}")
