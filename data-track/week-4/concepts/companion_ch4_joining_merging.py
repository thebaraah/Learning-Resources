import pandas as pd


def _make_tables():
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4],
            "customer_id": [100, 101, 999, 102],
            "product_id": ["A", "B", "A", "C"],
            "price_date": ["2024-01", "2024-01", "2024-02", "2024-02"],
            "amount": [120, 90, 200, 75],
        }
    )
    customers = pd.DataFrame(
        {
            "customer_id": [100, 101, 102],
            "name": ["Alice", "Bob", "Chloe"],
        }
    )
    prices = pd.DataFrame(
        {
            "product_id": ["A", "B", "C", "A"],
            "price_date": ["2024-01", "2024-01", "2024-02", "2024-02"],
            "unit_price": [10.0, 15.0, 20.0, 11.0],
        }
    )
    return orders, customers, prices


def section_1_join_types():
    print("--- Section: Join Types ---")
    orders, customers, _ = _make_tables()

    inner = orders.merge(customers, on="customer_id", how="inner")
    left = orders.merge(customers, on="customer_id", how="left")
    print(f"Inner join rows: {len(inner)}  (drops order with customer_id=999)")
    print(f"Left join rows:  {len(left)}   (keeps all orders, NaN for unmatched name)")
    print("\nLeft join result:")
    print(left)


def section_2_indicator():
    print("\n--- Section: Tracking Matches with indicator ---")
    orders, customers, _ = _make_tables()
    merged = orders.merge(customers, on="customer_id", how="left", indicator=True)
    print("_merge value counts:")
    print(merged["_merge"].value_counts())
    print("\nOrder with no matching customer:")
    print(merged[merged["_merge"] == "left_only"][["order_id", "customer_id"]])


def section_3_multi_key_join():
    print("\n--- Section: Joining on Multiple Keys ---")
    orders, _, prices = _make_tables()
    merged = orders.merge(prices, on=["product_id", "price_date"], how="left")
    print("Orders with unit_price added via product_id + price_date:")
    print(merged[["order_id", "product_id", "price_date", "amount", "unit_price"]])


def section_4_index_join():
    print("\n--- Section: Index-Based Joins ---")
    orders, customers, _ = _make_tables()
    customers_idx = customers.set_index("customer_id")
    orders_idx = orders.set_index("customer_id")
    merged = orders_idx.join(customers_idx, how="left")
    print("Index join result (customer_id is the index):")
    print(merged[["order_id", "name", "amount"]].reset_index())


def section_5_concat():
    print("\n--- Section: Concatenation ---")
    y2024 = pd.DataFrame({"order_id": [1, 2], "amount": [120, 90]})
    y2025 = pd.DataFrame({"order_id": [3, 4], "amount": [200, 75]})
    all_orders = pd.concat([y2024, y2025], ignore_index=True)
    print("Concatenated orders (index reset):")
    print(all_orders)

    # Many-to-many guard
    orders, customers, _ = _make_tables()
    merged = orders.merge(customers, on="customer_id", how="left")
    assert len(merged) == len(orders), "Row count should not change after left join"
    print("\nRow-count assertion passed: no unexpected row multiplication.")


if __name__ == "__main__":
    section_1_join_types()
    section_2_indicator()
    section_3_multi_key_join()
    section_4_index_join()
    section_5_concat()
