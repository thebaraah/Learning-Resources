import pandas as pd
from io import StringIO


def section_1_series_dataframe_index():
    print("--- Section: Pandas, Series, DataFrames, and Index ---")
    scores = pd.Series([90, 85, 70], name="score")
    print("Series:")
    print(scores)

    users = pd.DataFrame(
        {
            "user_id": [1, 2, 3],
            "name": ["Alice", "Bob", "Chloe"],
            "score": [90, 85, 70],
        }
    )
    print("\nDataFrame:")
    print(users)
    print("\nSelecting one column → Series:", type(users["name"]))
    print("Selecting two columns → DataFrame:", type(users[["name", "score"]]))


def section_2_creating_dataframes():
    print("\n--- Section: Creating DataFrames ---")
    users = pd.DataFrame(
        {
            "user_id": [1, 2, 3],
            "country": ["NL", "BE", "NL"],
        }
    )
    print("From dict of lists:")
    print(users)

    orders = pd.DataFrame(
        [
            {"order_id": 101, "amount": 120.0},
            {"order_id": 102, "amount": 90.0},
        ]
    )
    print("\nFrom list of dicts:")
    print(orders)

    orders_csv = pd.read_csv(StringIO("order_id,amount\n101,120.0\n102,90.0\n103,45.5"))
    print("\nFrom CSV string:")
    print(orders_csv)


def section_3_inspecting_data():
    print("\n--- Section: Inspecting Data Quickly ---")
    orders = pd.read_csv(StringIO("order_id,amount\n101,120.0\n102,90.0\n103,45.5\n104,200.0\n105,33.0"))

    print("head(3):")
    print(orders.head(3))
    print("\nshape:", orders.shape)
    print("\ndtypes:\n", orders.dtypes)
    print("\ndescribe():")
    print(orders.describe())
    # info() writes to stdout directly
    print("\ninfo():")
    orders.info()


def section_4_missing_data():
    print("\n--- Section: Missing Data Basics ---")
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4],
            "amount": [120.0, None, 75.0, 200.0],
            "region": ["NL", "BE", None, "DE"],
        }
    )
    print("Missing values per column:")
    print(orders.isna().sum())

    orders["amount"] = orders["amount"].fillna(0)
    orders = orders.dropna(subset=["region"])
    print("\nAfter fillna(0) on amount and dropna on region:")
    print(orders)


def section_5_column_operations():
    print("\n--- Section: Basic Column Operations ---")
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "amount": [120.0, 90.0, 200.0],
        }
    )
    orders["amount_eur"] = orders["amount"] * 0.92
    orders["is_big_order"] = orders["amount"] > 100
    orders = orders.assign(amount_usd=lambda df: df["amount"] * 1.1)
    print(orders)


if __name__ == "__main__":
    section_1_series_dataframe_index()
    section_2_creating_dataframes()
    section_3_inspecting_data()
    section_4_missing_data()
    section_5_column_operations()
