"""Exercise 4: Joining Two Tables.

Merge the orders DataFrame with a customers table, then analyse
which customer segment drives the most orders.
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

customers = pd.DataFrame(
    {
        "customer_id": [100, 101, 102, 103],
        "name": ["Alice", "Bob", "Chloe", "Daan"],
        "segment": ["retail", "retail", "b2b", "b2b"],
    }
)

# TODO 1: Join orders with customers using a left join on customer_id.
# Assign the result to enriched and print it.

# WHY left join: a left join keeps ALL rows from the left table (orders)
# regardless of whether a match exists in the right table (customers).
# An inner join would silently drop any order whose customer_id is not in
# the customers table — a data loss you might not notice immediately.
# In analytics, losing rows at join time is a common silent failure.
# Default for pd.merge is an inner join, so you must say how='left' explicitly.
enriched = pd.merge(orders, customers, on="customer_id", how="left")
print(enriched)

# TODO 2: Count how many orders belong to each segment.
# Use groupby('segment').size() or value_counts().
# Print the result.

# WHY .size() not .count(): .count() counts non-null values per column and
# returns a multi-column result. .size() counts rows per group (regardless of
# nulls), which is exactly "how many orders" per segment.
# WHY dropna=False: the left join above preserves unmatched orders as NaN in
# 'segment'. Without dropna=False, groupby silently drops those rows — the same
# kind of silent data loss we used the left join to avoid.
segment_counts = enriched.groupby("segment", dropna=False).size().sort_values(ascending=False)
print(segment_counts)
