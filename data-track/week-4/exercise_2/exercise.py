"""Exercise 2: Filtering and Sorting.

Filter, sort, and annotate the orders DataFrame from Exercise 1.
Paste the setup block below into your script, then work through the TODOs.
"""
from io import StringIO

import pandas as pd

# Setup block (same dataset as Exercise 1, amount NaN filled)
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

# TODO 1: Filter orders where region is 'NL' AND amount is greater than 80.
# Use a boolean mask (two conditions combined with &).
# Assign the result to nl_big.

# TODO 2: Sort nl_big by amount descending.
# Assign the sorted result to nl_big_sorted.
# Print nl_big_sorted.

# TODO 3: Add a column 'is_big_order' to the original orders DataFrame.
# It should be True where amount >= 150, False otherwise.
# Print orders[['order_id', 'amount', 'is_big_order']].

# Expected nl_big_sorted:
#    order_id  customer_id region  amount  order_date
# 0         1          100     NL   120.0  2024-01-02

# Expected is_big_order column (only order_id 4 is >= 150):
#    order_id  amount  is_big_order
# 0         1   120.0         False
# 1         2    90.0         False
# 2         3     0.0         False
# 3         4   200.0          True
# 4         5    50.0         False
