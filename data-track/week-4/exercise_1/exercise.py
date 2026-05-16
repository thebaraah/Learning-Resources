"""Exercise 1: Quick EDA on Orders.

You have a small orders dataset with a missing value. Explore it with
pandas and fix the gap before moving on to later exercises.

Exercises 2-5 build on the `orders` DataFrame you create here. Run
this file first (or paste the setup block into your own script).
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

# TODO 2: Count missing values per column.
# Hint: combine .isnull() and .sum().

# TODO 3: Fill missing 'amount' values with 0.
# Use fillna() and reassign (or use inplace=True).

# Expected output after all three TODOs:
# --- info ---
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# ...   amount  4 non-null   float64
# ...
# --- describe ---
#        order_id  customer_id  amount
# count       5.0          5.0     4.0
# ...
# --- missing values ---
# order_id      0
# customer_id   0
# region        0
# amount        1
# order_date    0
# dtype: int64
# --- after fill ---
# amount    0
# dtype: int64
