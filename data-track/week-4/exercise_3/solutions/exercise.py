"""Exercise 3: Grouping and Aggregation.

Aggregate the orders DataFrame by region, then add a derived column
using transform so every row knows its region's average.
"""
from io import StringIO

import pandas as pd

# Setup block
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

# TODO 1: Group by 'region' and calculate total revenue and order count.
# Use groupby().agg() with a dict: {'amount': ['sum', 'count']}.
# Assign the result to region_summary and print it.

# WHY agg() over two separate groupby calls: agg() with a list of functions
# computes all aggregations in a single pass and returns a clean multi-level
# column DataFrame. Two separate calls would produce two objects you then
# have to join manually.
region_summary = orders.groupby("region").agg({"amount": ["sum", "count"]})
print(region_summary)

# TODO 2: Add a column 'region_avg' to the original orders DataFrame
# with the average order amount per region.
# Use groupby().transform('mean') so the result aligns with the original index.
# Assign to orders['region_avg'].

# WHY transform not agg: agg collapses the DataFrame to one row per group.
# transform returns a Series with the SAME length as the original DataFrame,
# matching each row to its group's result. That is what you need to add a
# column back to the original 5-row DataFrame without losing any rows.
orders["region_avg"] = orders.groupby("region")["amount"].transform("mean")

# TODO 3: Verify that 'region_avg' is the same for all rows in the same region.
# Print orders[['order_id', 'region', 'amount', 'region_avg']].
print(orders[["order_id", "region", "amount", "region_avg"]])
