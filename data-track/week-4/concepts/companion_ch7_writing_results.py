import sqlite3
import tempfile
from pathlib import Path

import pandas as pd


def _make_df():
    return pd.DataFrame(
        {
            "region": ["NL", "BE", "DE"],
            "month": ["2024-01", "2024-01", "2024-01"],
            "total_revenue": [320.0, 140.0, 200.0],
            "order_count": [4, 2, 1],
        }
    )


def section_1_write_csv():
    print("--- Section: Writing CSV Files ---")
    monthly_sales = _make_df()
    with tempfile.TemporaryDirectory() as tmp:
        output_path = Path(tmp) / "monthly_sales.csv"
        monthly_sales.to_csv(output_path, index=False)
        check = pd.read_csv(output_path)
        assert list(check.columns) == list(monthly_sales.columns), "Column mismatch"
        assert len(check) == len(monthly_sales)
        print(f"CSV written and verified: {len(check)} rows, columns: {list(check.columns)}")
        # Unnamed: 0 appears when index=True; confirm it is absent
        assert "Unnamed: 0" not in check.columns, "Index leaked into CSV"
        print("No spurious index column.")


def section_2_write_parquet():
    print("\n--- Section: Writing Parquet Files ---")
    monthly_sales = _make_df()
    with tempfile.TemporaryDirectory() as tmp:
        parquet_path = Path(tmp) / "monthly_sales.parquet"
        monthly_sales.to_parquet(parquet_path, index=False)
        check = pd.read_parquet(parquet_path)
        assert len(check) == len(monthly_sales)
        print(f"Parquet written and verified: {len(check)} rows")
        print("dtypes preserved:")
        print(check.dtypes)


def section_3_write_sqlite():
    print("\n--- Section: Writing to SQLite ---")
    monthly_sales = _make_df()
    with tempfile.TemporaryDirectory() as tmp:
        db_path = Path(tmp) / "analytics.db"
        with sqlite3.connect(db_path) as conn:
            monthly_sales.to_sql("monthly_sales", conn, if_exists="replace", index=False)
        # Read back to confirm
        with sqlite3.connect(db_path) as conn:
            check = pd.read_sql("SELECT * FROM monthly_sales", conn)
        assert len(check) == len(monthly_sales)
        print(f"SQLite written and verified: {len(check)} rows")
        print(check)


def section_4_validate_roundtrip():
    print("\n--- Section: Validate What You Wrote ---")
    monthly_sales = _make_df()
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "monthly_sales.parquet"
        monthly_sales.to_parquet(path, index=False)
        check = pd.read_parquet(path)
        assert len(check) == len(monthly_sales)
        assert list(check.columns) == list(monthly_sales.columns)
        print("Read-back assertion passed: row count and columns match.")


if __name__ == "__main__":
    section_1_write_csv()
    section_2_write_parquet()
    section_3_write_sqlite()
    section_4_validate_roundtrip()
