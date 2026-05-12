"""Exercise 3: Read and Normalize File Formats.

You receive weather readings in two formats. The field names differ. Your job
is to normalize both into a single shape your pipeline can consume.

The sample files ship next to this script:
  - data/stations.csv: columns `station_name`, `temp`, `humidity`, `date`
  - data/readings.json: list of objects with keys `station`,
    `temperature_c`, `humidity_pct`, `timestamp`

Steps:
  1. Write `read_csv_file(path) -> list[dict]` that loads the CSV into
     row-dicts. Hint: `csv.DictReader`.
  2. Write `read_json_file(path) -> list[dict]` that loads the JSON list.
  3. Write `normalize_record(record: dict) -> dict` that maps any input
     into a single shape:
       {"station": str, "temperature_c": float, "humidity_pct": int,
        "timestamp": str}
  4. Run both readers, normalize each row, and print the combined list.

Hint: use `record.get("first_key", record.get("fallback_key"))` to handle
multiple possible source field names.
"""
from __future__ import annotations

from pathlib import Path


DATA_DIR = Path(__file__).parent / "data"


# TODO 1: read_csv_file
def read_csv_file(path: Path | str) -> list[dict]:
    """Return the CSV at `path` as a list of row dicts."""
    raise NotImplementedError("Implement me with csv.DictReader.")


# TODO 2: read_json_file
def read_json_file(path: Path | str) -> list[dict]:
    """Return the JSON file at `path` as a list of dicts."""
    raise NotImplementedError("Implement me with json.load.")


# TODO 3: normalize_record
def normalize_record(record: dict) -> dict:
    """Map any source row into the canonical pipeline shape."""
    raise NotImplementedError("Implement me with chained .get() fallbacks.")


if __name__ == "__main__":
    csv_rows = read_csv_file(DATA_DIR / "stations.csv")
    json_rows = read_json_file(DATA_DIR / "readings.json")
    print(f"CSV rows: {len(csv_rows)}  JSON rows: {len(json_rows)}")

    normalized = [normalize_record(r) for r in csv_rows + json_rows]
    for row in normalized:
        print(row)

    # Expected after refactor: every printed row has keys
    #   station, temperature_c, humidity_pct, timestamp
    # regardless of whether it came from CSV or JSON.
