import tempfile
from pathlib import Path

import pandas as pd


def section_1_polars():
    print("--- Section: Polars ---")
    import polars as pl

    orders = pl.DataFrame(
        {
            "region": ["NL", "NL", "BE", "DE"],
            "amount": [120, 80, 90, 200],
        }
    )
    result = (
        orders
        .group_by("region")
        .agg(pl.col("amount").sum().alias("total_revenue"))
        .sort("region")
    )
    print("Polars groupby result:")
    print(result)

    # Round-trip: Polars → Pandas → Polars
    pandas_df = result.to_pandas()
    back_to_polars = pl.from_pandas(pandas_df)
    print(f"\nConverted to Pandas ({type(pandas_df).__name__}) and back to Polars ({type(back_to_polars).__name__}).")


def section_2_duckdb():
    print("\n--- Section: DuckDB ---")
    import duckdb

    with tempfile.TemporaryDirectory() as tmp:
        sample_path = Path(tmp) / "orders.csv"
        pd.DataFrame(
            {"region": ["NL", "NL", "BE", "DE"], "amount": [120, 80, 90, 200]}
        ).to_csv(sample_path, index=False)

        # Query a CSV file directly (no explicit Pandas load)
        result = duckdb.sql(
            f"""
            SELECT region, SUM(amount) AS total_revenue
            FROM '{sample_path}'
            GROUP BY region
            ORDER BY region
            """
        ).df()
        print("DuckDB query on CSV file (no prior Pandas load):")
        print(result)

    # Register a Pandas DataFrame with DuckDB
    orders_pd = pd.DataFrame(
        {"region": ["NL", "NL", "BE", "DE"], "amount": [120, 80, 90, 200]}
    )
    con = duckdb.connect()
    con.register("orders", orders_pd)
    duckdb_result = con.execute(
        "SELECT region, SUM(amount) AS total_revenue FROM orders GROUP BY region ORDER BY region"
    ).df()
    print("\nDuckDB query on registered Pandas DataFrame:")
    print(duckdb_result)


def section_3_dask():
    print("\n--- Section: Dask ---")
    import dask.dataframe as dd

    _df = pd.DataFrame(
        {"region": ["NL", "NL", "BE", "DE"], "amount": [120, 80, 90, 200]}
    )
    orders = dd.from_pandas(_df, npartitions=2)
    result = orders.groupby("region")["amount"].sum().compute()
    print("Dask groupby result:")
    print(result.sort_index())


def section_4_comparison():
    print("\n--- Section: Quick Comparison ---")
    # Show identical groupby output from all four tools, sorted for easy comparison
    import duckdb
    import polars as pl
    import dask.dataframe as dd

    data = {"region": ["NL", "NL", "BE", "DE"], "amount": [120, 80, 90, 200]}

    pandas_result = (
        pd.DataFrame(data).groupby("region")["amount"].sum()
        .reset_index().rename(columns={"amount": "total"}).sort_values("region")
    )

    polars_result = (
        pl.DataFrame(data).group_by("region").agg(pl.col("amount").sum().alias("total"))
        .sort("region").to_pandas()
    )

    dask_result = (
        dd.from_pandas(pd.DataFrame(data), npartitions=1)
        .groupby("region")["amount"].sum().compute()
        .reset_index().rename(columns={"amount": "total"}).sort_values("region")
    )

    con = duckdb.connect()
    con.register("orders", pd.DataFrame(data))
    duck_result = con.execute(
        "SELECT region, SUM(amount) AS total FROM orders GROUP BY region ORDER BY region"
    ).df()

    print("Pandas:"); print(pandas_result.to_string(index=False))
    print("Polars:"); print(polars_result.to_string(index=False))
    print("Dask:  "); print(dask_result.to_string(index=False))
    print("DuckDB:"); print(duck_result.to_string(index=False))
    print("\nAll four produce the same totals.")


if __name__ == "__main__":
    section_1_polars()
    section_2_duckdb()
    section_3_dask()
    section_4_comparison()
