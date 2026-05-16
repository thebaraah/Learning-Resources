"""Exercise 7: Visualize Revenue.

Plot total revenue by region as a bar chart and save it to disk.
Uses the non-interactive 'Agg' backend so it works in headless
environments (Codespaces, CI, servers).
"""
from io import StringIO
from pathlib import Path

import matplotlib
matplotlib.use("Agg")   # must come before importing pyplot
import matplotlib.pyplot as plt
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
Path("output").mkdir(exist_ok=True)

# TODO 1: Group orders by 'region' and sum 'amount'.
# Plot the result as a bar chart using .plot(kind='bar').
# Assign the axes object returned by .plot() to ax.

# TODO 2: Add axis labels and a title.
# x-axis label: 'Region'
# y-axis label: 'Total Revenue (€)'
# Title: 'Revenue by Region'

# TODO 3: Call plt.tight_layout() then save to 'output/revenue_by_region.png'.
# Confirm the file exists by printing Path("output/revenue_by_region.png").exists().

# Expected: output/revenue_by_region.png is created and .exists() returns True.
# Bar heights: NL=170, DE=200, BE=90 (NL has three orders, one with amount=0).
