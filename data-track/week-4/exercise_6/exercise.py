"""Exercise 6: Strings and Dates.

Practise the .str accessor (email normalisation) and the .dt accessor
(extracting date parts and filtering by date).
"""
from io import StringIO

import pandas as pd

# Setup block (extends orders with email + datetime column)
_csv = StringIO(
    """order_id,customer_id,region,amount,order_date
1,100,NL,120,2024-01-02
2,101,BE,90,2024-01-03
3,102,NL,,2024-01-03
4,103,DE,200,2024-01-04
5,100,NL,50,2024-01-05
"""
)
orders = pd.read_csv(_csv)
orders["amount"] = orders["amount"].fillna(0)
orders["email"] = [
    "alice@example.com",
    "BOB@Example.COM",
    None,
    "daan@example.nl",
    "alice@example.com",
]
orders["order_date"] = pd.to_datetime(orders["order_date"])

# TODO 1: Normalize the 'email' column to lowercase with no leading/trailing
# whitespace. Use .str.strip() then .str.lower() — both skip NaN by default
# and leave missing values as NaN in the output.
# Assign the result back to orders['email'].
# Print orders[['order_id', 'email']].

# TODO 2: Extract the year and month from 'order_date' into two new columns:
# 'year' and 'month'. Use the .dt accessor.
# Print orders[['order_id', 'order_date', 'year', 'month']].

# TODO 3: Filter to orders placed in January 2024 using the .dt accessor.
# Assign the filtered result to jan_orders and print it.

# Expected email after normalisation:
#    order_id              email
# 0         1  alice@example.com
# 1         2    bob@example.com
# 2         3               None  (NaN)
# 3         4    daan@example.nl
# 4         5  alice@example.com

# Expected jan_orders: all 5 rows (all dates are in January 2024)
