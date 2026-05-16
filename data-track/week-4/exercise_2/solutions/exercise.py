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

# WHY &, not 'and': pandas evaluates conditions element-wise across the whole
# column. Python's 'and' is a scalar operator and raises an ambiguous truth-
# value error on a Series. The bitwise & operator applies per element, which
# is exactly what you want here.
nl_big = orders[(orders["region"] == "NL") & (orders["amount"] > 80)]

# TODO 2: Sort nl_big by amount descending.
# Assign the sorted result to nl_big_sorted.
# Print nl_big_sorted.

# WHY ascending=False: sort_values sorts ascending by default.
# Passing ascending=False gives highest amount first, which is the natural
# "show me the biggest orders" view.
nl_big_sorted = nl_big.sort_values("amount", ascending=False)
print(nl_big_sorted)

# TODO 3: Add a column 'is_big_order' to the original orders DataFrame.
# It should be True where amount >= 150, False otherwise.
# Print orders[['order_id', 'amount', 'is_big_order']].

# WHY a boolean column not a filtered subset: annotating the original DataFrame
# lets downstream code filter on is_big_order without knowing the threshold.
# It also keeps all rows together so you can still see small orders in context.
orders["is_big_order"] = orders["amount"] >= 150
print(orders[["order_id", "amount", "is_big_order"]])
