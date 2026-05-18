import pandas as pd


def section_1_selecting_columns():
    print("--- Section: Selecting Columns ---")
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "country": ["NL", "BE", "DE", "NL", "BE"],
            "amount": [45, 120, 75, 210, 180],
        }
    )
    print("Single column (Series):")
    print(orders["amount"])
    print("\nMultiple columns (DataFrame):")
    print(orders[["order_id", "amount"]])


def section_2_loc_iloc():
    print("\n--- Section: Selecting Rows with loc and iloc ---")
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "country": ["NL", "BE", "DE", "NL", "BE"],
            "amount": [45, 120, 75, 210, 180],
        }
    )
    print("loc[0]: row with label 0:")
    print(orders.loc[0])
    print("\nloc[0:2, ['order_id','amount']]: labels 0-2 inclusive:")
    print(orders.loc[0:2, ["order_id", "amount"]])
    print("\niloc[0:3, 0:2]: positions 0-2 exclusive, first 2 columns:")
    print(orders.iloc[0:3, 0:2])
    # loc includes end; iloc does not: show the difference
    print("\nloc[0:2] row count:", len(orders.loc[0:2]))   # 3
    print("iloc[0:2] row count:", len(orders.iloc[0:2]))   # 2 - end exclusive


def section_3_boolean_filtering():
    print("\n--- Section: Boolean Filtering ---")
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "country": ["NL", "BE", "DE", "NL", "BE"],
            "amount": [45, 120, 75, 210, 180],
        }
    )
    big_orders = orders[orders["amount"] > 100]
    print("Orders with amount > 100:")
    print(big_orders)

    # Python `and` tries to reduce the whole Series to a single bool — raises ValueError.
    try:
        _ = orders[orders["country"] == "NL" and orders["amount"] > 100]
    except ValueError as e:
        print(f"\nBAD — `and` raises ValueError: {e}")

    nl_big = orders[(orders["country"] == "NL") & (orders["amount"] > 100)]
    print("\nGOOD — `&` with parentheses works:")
    print(nl_big)

    # query alternative
    query_result = orders.query("country == 'NL' and amount > 100")
    print("\nSame filter via query():")
    print(query_result)


def section_4_sorting_ranking():
    print("\n--- Section: Sorting and Ranking ---")
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "country": ["NL", "BE", "DE", "NL", "BE"],
            "amount": [45, 120, 75, 120, 180],
        }
    )
    print("Sorted by amount descending:")
    print(orders.sort_values("amount", ascending=False))

    print("\nSorted by country asc, amount desc:")
    print(orders.sort_values(["country", "amount"], ascending=[True, False]))

    orders["rank_dense"] = orders["amount"].rank(ascending=False, method="dense")
    orders["rank_min"] = orders["amount"].rank(ascending=False, method="min")
    print("\nWith dense and min ranks (note tied 120 values):")
    print(orders[["order_id", "amount", "rank_dense", "rank_min"]])


def section_5_duplicates():
    print("\n--- Section: Duplicates ---")
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 2, 3, 4],
            "amount": [45, 120, 120, 75, 210],
        }
    )
    print("Duplicate order_id count:", orders.duplicated(subset=["order_id"]).sum())
    deduped = orders.drop_duplicates(subset=["order_id"])
    print("After drop_duplicates on order_id:")
    print(deduped)


if __name__ == "__main__":
    section_1_selecting_columns()
    section_2_loc_iloc()
    section_3_boolean_filtering()
    section_4_sorting_ranking()
    section_5_duplicates()
