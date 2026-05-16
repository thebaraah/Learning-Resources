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

# WHY chain .str methods: pandas .str accessor works element-wise on every
# non-null value. Both .str.strip() and .str.lower() skip NaN cells and
# propagate them unchanged in the output, which is the correct "no email"
# representation. You do not need any special flag — NaN pass-through is
# the default behaviour of all .str accessor methods.
orders["email"] = orders["email"].str.strip().str.lower()
print(orders[["order_id", "email"]])

# TODO 2: Extract the year and month from 'order_date' into two new columns.

# WHY .dt accessor: after pd.to_datetime(), a pandas Series stores timestamps
# internally. The .dt accessor exposes datetime properties (year, month, day,
# hour, etc.) as integer Series without needing to call strftime or apply().
# It is vectorised and much faster than a row-by-row lambda.
orders["year"] = orders["order_date"].dt.year
orders["month"] = orders["order_date"].dt.month
print(orders[["order_id", "order_date", "year", "month"]])

# TODO 3: Filter to orders placed in January 2024 using the .dt accessor.

# WHY both conditions (month AND year): filtering only on month would include
# January from every year in a multi-year dataset. Being explicit about both
# makes the filter self-documenting and safe to paste into longer pipelines.
jan_orders = orders[(orders["order_date"].dt.month == 1) & (orders["order_date"].dt.year == 2024)]
print(jan_orders)
