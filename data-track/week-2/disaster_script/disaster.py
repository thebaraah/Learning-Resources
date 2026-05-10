"""Week 2 §2 - The Disaster Script.

Count the problems together on the whiteboard:
  1. Hardcoded path
  2. Magic number 0.21 (VAT rate)
  3. No way to test the VAT calc without a CSV file
  4. Mutates rows in place (side effects)
  5. price = 'ten' would crash silently with no useful message
"""

import csv

data = []
with open("/Users/steve/Downloads/sales.csv") as f:
    for row in csv.DictReader(f):
        data.append(row)

for row in data:
    row["product_name"] = row["product_name"].strip().title()
    row["price"] = float(row["price"])
    row["revenue"] = row["price"] * int(row["quantity"])
    row["vat"] = row["revenue"] * 0.21

with open("clean.csv", "w") as f:
    w = csv.DictWriter(f, fieldnames=data[0].keys())
    w.writeheader()
    w.writerows(data)
