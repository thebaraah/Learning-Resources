import pandas as pd


def _make_orders():
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5, 6, 7],
            "customer_id": [10, 10, 10, 20, 20, 30, 30],
            "region": ["NL", "NL", "BE", "DE", "NL", "BE", "NL"],
            "month": ["2024-01", "2024-01", "2024-01", "2024-02", "2024-02", "2024-02", "2024-02"],
            "order_date": pd.to_datetime(
                ["2024-01-05", "2024-01-12", "2024-01-20", "2024-02-03",
                 "2024-02-14", "2024-02-18", "2024-02-25"]
            ),
            "amount": [120, 80, 90, 200, 150, 50, 95],
        }
    )


def section_1_groupby_pattern():
    print("--- Section: The groupby Pattern ---")
    orders = _make_orders()
    summary = (
        orders.groupby(["region", "month"], as_index=False)
        .agg(
            total_revenue=("amount", "sum"),
            avg_order_value=("amount", "mean"),
            order_count=("order_id", "count"),
        )
    )
    print(summary.to_string(index=False))


def section_2_multiple_aggregations():
    print("\n--- Section: Multiple Aggregations ---")
    orders = _make_orders()
    metrics = orders.groupby("region").agg(
        total=("amount", "sum"),
        max_order=("amount", "max"),
        first_order_date=("order_date", "min"),
    )
    print(metrics)


def section_3_size_vs_count():
    print("\n--- Section: size() vs count() ---")
    orders = _make_orders()
    # Introduce one NaN in amount to show the difference
    orders.loc[0, "amount"] = None

    print("size() (includes NaN rows):")
    print(orders.groupby("region").size())
    print("\ncount() on amount (ignores NaN):")
    print(orders.groupby("region")["amount"].count())


def section_4_transform():
    print("\n--- Section: Transform vs Aggregate ---")
    orders = _make_orders()
    orders["region_avg"] = orders.groupby("region")["amount"].transform("mean")
    print("Each order with its region's average amount:")
    print(orders[["order_id", "region", "amount", "region_avg"]])
    print("Row count unchanged:", len(orders))


def section_5_filter_groups():
    print("\n--- Section: Filtering Groups ---")
    orders = _make_orders()
    # Keep only customers with 3+ orders
    high_volume = orders.groupby("customer_id").filter(lambda group: len(group) >= 3)
    print("Customers with 3+ orders (customer_id 10 only):")
    print(high_volume[["order_id", "customer_id", "amount"]])


if __name__ == "__main__":
    section_1_groupby_pattern()
    section_2_multiple_aggregations()
    section_3_size_vs_count()
    section_4_transform()
    section_5_filter_groups()
