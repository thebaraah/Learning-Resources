import pandas as pd


def _make_orders():
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5, 6],
            "customer_id": [10, 10, 20, 20, 30, 30],
            "country": ["NL", "BE", "NL", "DE", "BE", "NL"],
            "month": ["2024-01", "2024-01", "2024-02", "2024-02", "2024-03", "2024-03"],
            "channel": ["web", "app", "web", "app", "web", "app"],
            "order_date": pd.to_datetime(
                ["2024-01-05", "2024-01-12", "2024-02-03", "2024-02-18",
                 "2024-03-07", "2024-03-22"]
            ),
            "amount": [120, 80, 200, 150, 90, 95],
        }
    )


def section_1_pivot_melt():
    print("--- Section: Pivot and Melt ---")
    sales = pd.DataFrame(
        {
            "customer_id": [10, 10, 20, 20],
            "month": ["2024-01", "2024-02", "2024-01", "2024-02"],
            "amount": [120, 150, 90, 110],
        }
    )
    pivoted = sales.pivot(index="customer_id", columns="month", values="amount")
    print("Pivoted (long → wide):")
    print(pivoted)

    long = pivoted.reset_index().melt(
        id_vars="customer_id",
        var_name="month",
        value_name="amount",
    )
    print("\nMelted back (wide → long):")
    print(long.sort_values(["customer_id", "month"]).reset_index(drop=True))


def section_2_pivot_table():
    print("\n--- Section: pivot_table for Aggregations ---")
    orders = _make_orders()
    summary = orders.pivot_table(
        index="country",
        columns="channel",
        values="amount",
        aggfunc="sum",
        fill_value=0,
    )
    print("Total amount per country × channel:")
    print(summary)


def section_3_mapping():
    print("\n--- Section: Mapping and Applying Functions ---")
    orders = _make_orders()
    region_map = {"NL": "Europe", "BE": "Europe", "DE": "Europe", "US": "North America"}
    orders["region_group"] = orders["country"].map(region_map).fillna("Other")
    print(orders[["order_id", "country", "region_group"]])


def section_4_window_functions():
    print("\n--- Section: Window Functions ---")
    orders = _make_orders().sort_values("order_date").reset_index(drop=True)
    orders["rolling_3"] = orders["amount"].rolling(3, min_periods=1).sum()
    orders["cumulative"] = orders["amount"].cumsum()
    orders["prev_amount"] = orders["amount"].shift(1)
    print(orders[["order_id", "order_date", "amount", "rolling_3", "cumulative", "prev_amount"]])


def section_5_vectorization():
    print("\n--- Section: Vectorization vs Loops ---")
    orders = _make_orders()

    # Slow loop approach (functional result identical to vectorized)
    orders["amount_usd_loop"] = [amount * 1.1 for amount in orders["amount"]]

    # Vectorized
    orders["amount_usd_vec"] = orders["amount"] * 1.1

    # Results must be identical
    assert (orders["amount_usd_loop"] == orders["amount_usd_vec"]).all()
    print("Loop and vectorized results are identical.")
    print(orders[["order_id", "amount", "amount_usd_vec"]])


if __name__ == "__main__":
    section_1_pivot_melt()
    section_2_pivot_table()
    section_3_mapping()
    section_4_window_functions()
    section_5_vectorization()
