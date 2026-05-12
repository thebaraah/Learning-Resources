"""Exercise 3 — Reference solution.

Read the `# WHY ...:` notes, not the code.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path


DATA_DIR = Path(__file__).parent.parent / "data"
# WHY .parent.parent: this file lives under solutions/. The shared fixture
# data sits one level up (next to the starter), so we go up two parents.


# TODO 1: read_csv_file
def read_csv_file(path: Path | str) -> list[dict]:
    """Return the CSV at `path` as a list of row dicts."""
    # WHY DictReader over csv.reader: DictReader pairs each row with the
    # header automatically. csv.reader would force us to zip headers manually
    # on every row and is more error-prone.
    # WHY newline="": Python's docs are explicit that csv readers must open
    # files with newline="" to avoid double-handling line endings on Windows.
    # WHY encoding="utf-8": be explicit; the platform default is unreliable
    # across Windows (cp1252) / Linux / macOS.
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# TODO 2: read_json_file
def read_json_file(path: Path | str) -> list[dict]:
    """Return the JSON file at `path` as a list of dicts."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    # WHY check isinstance(list): a defensive reader handles the case where
    # the source wraps the list in {"results": [...]}. The chapter shows the
    # full version; here we just trust the contract.
    if not isinstance(data, list):
        raise ValueError(f"Expected a list, got {type(data).__name__}")
    return data


# TODO 3: normalize_record
def normalize_record(record: dict) -> dict:
    """Map any source row into the canonical pipeline shape."""
    # WHY chained .get(): each source uses different keys. record.get("station",
    # record.get("station_name")) reads as "first try station, fall back to
    # station_name". The first match wins.
    # WHY cast types explicitly: CSV values are always strings (`"18.5"` and
    # `"72"`), so float()/int() coerce them. JSON already has the right types,
    # but float(18.5) is a no-op so this is safe to apply to both.
    return {
        "station": str(record.get("station") or record.get("station_name", "unknown")),
        "temperature_c": float(record.get("temperature_c") or record.get("temp")),
        "humidity_pct": int(record.get("humidity_pct") or record.get("humidity")),
        "timestamp": str(record.get("timestamp") or record.get("date", "")),
    }


if __name__ == "__main__":
    csv_rows = read_csv_file(DATA_DIR / "stations.csv")
    json_rows = read_json_file(DATA_DIR / "readings.json")
    print(f"CSV rows: {len(csv_rows)}  JSON rows: {len(json_rows)}")

    normalized = [normalize_record(r) for r in csv_rows + json_rows]
    for row in normalized:
        print(row)

    # Expected: 5 lines printed, each carrying the four canonical keys.
