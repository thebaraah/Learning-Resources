"""Exercise 1: Quick EDA on Orders.

You have a small orders dataset with a missing value. Explore it with
pandas and fix the gap before moving on to later exercises.

Each exercise is self-contained with its own embedded dataset.
You do not need to run this file before attempting the others.
"""
from io import StringIO

import pandas as pd

csv_data = StringIO(
    """order_id,customer_id,region,amount,order_date
1,100,NL,120,2024-01-02
2,101,BE,90,2024-01-03
3,102,NL,,2024-01-03
4,103,DE,200,2024-01-04
5,100,NL,50,2024-01-05
"""
)

orders = pd.read_csv(csv_data)

# TODO 1: Call orders.info() and orders.describe() and print the results.
# What dtype does pandas infer for 'amount'? What does describe() say about it?

# WHY print + describe separately: info() prints directly to stdout; describe()
# returns a DataFrame. Separating them with a header makes the output readable.
print("--- info ---")
orders.info()
print()
print("--- describe ---")
print(orders.describe())

# TODO 2: Count missing values per column.
# Hint: combine .isnull() and .sum().

# WHY isnull().sum(): isnull() returns a boolean DataFrame (True where NaN);
# sum() treats True as 1, so it counts the missing values per column in one line.
print()
print("--- missing values ---")
print(orders.isnull().sum())

# TODO 3: Fill missing 'amount' values with 0.
# Use fillna() and reassign (or use inplace=True).

# WHY fillna(0) not dropna(): dropping row 3 entirely would lose the order.
# Filling with 0 keeps the row visible so downstream analysts can decide whether
# the missing amount means "no sale" or "data error". A 0 in the data is
# explicit; a dropped row is invisible.
orders["amount"] = orders["amount"].fillna(0)

print()
print("--- after fill ---")
print(orders.isnull().sum())
