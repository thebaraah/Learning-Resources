# Exercise 5: Reshape and Export

**Concepts:** `pivot_table`, file output (CSV + Parquet).

## Setup

The setup block in `exercise.py` creates `orders`, parses `order_date` as datetime, and creates the `output/` folder. No extra setup needed.

## Task

1. Create a pivot table of total `amount` by `region` (rows) and `order_date` (columns) using `pd.pivot_table()` with `aggfunc='sum'`.
2. Save the pivot table to `output/pivot.csv` and `output/pivot.parquet`.
3. Read the Parquet file back with `pd.read_parquet()` and print its row count.

## Success criteria

- `pivot` has 3 rows (one per region: BE, DE, NL) and 4 columns (one per unique date).
- Both `output/pivot.csv` and `output/pivot.parquet` are created in the `output/` folder.
- The re-read Parquet DataFrame has 3 rows.

## Note

`to_parquet()` requires the `pyarrow` package. It is listed in `requirements.txt`.

## Stretch

- Open `output/pivot.csv` in a text editor. What does pandas write for missing date/region combinations (NaN)?
- Compare file sizes: `pivot.csv` vs `pivot.parquet`. Which is smaller and why?
