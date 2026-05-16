"""Exercise 5: Reshape and Export.

Create a pivot table from the orders data, then write it to CSV and
Parquet formats. Read the Parquet file back to confirm round-trip fidelity.
"""
from io import StringIO
from pathlib import Path

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
orders["order_date"] = pd.to_datetime(orders["order_date"])

output_dir = Path(__file__).resolve().parent / "output"
output_dir.mkdir(exist_ok=True)

# TODO 1: Create a pivot table of total 'amount' by 'region' (rows) and
# 'order_date' (columns). Use pd.pivot_table() with aggfunc='sum'.
# Assign the result to pivot and print it.

# TODO 2: Save pivot to output_dir / 'pivot.csv' and output_dir / 'pivot.parquet'.
# Use to_csv() and to_parquet() respectively.

# TODO 3: Read back the Parquet file from output_dir / 'pivot.parquet' and
# confirm the row count matches. Print the row count of the re-read DataFrame.

# Expected pivot shape: 3 rows (BE, DE, NL), columns = unique order dates.
# Expected Parquet row count: 3
