# Exercise 3: Grouping and Aggregation

**Concepts:** `groupby`, `agg`, `transform`.

## Setup

The setup block at the top of `exercise.py` creates and cleans the `orders` DataFrame.

## Task

1. Group `orders` by `region` and calculate total revenue (`sum`) and order count with `groupby().agg()`.
2. Add a column `region_avg` to `orders` using `groupby().transform('mean')`. This should give every row its region's average, not a summary table.
3. Print the full DataFrame showing `order_id`, `region`, `amount`, and `region_avg` and confirm that all NL rows have the same `region_avg`.

## Success criteria

- `region_summary` shows NL total = 170.0 (120 + 0 + 50) and count = 3.
- `orders['region_avg']` is the same (approximately 56.67) for all three NL rows.
- The DataFrame keeps all 5 rows (transform does not collapse them).

## Stretch

- What is the difference between `groupby().agg()` and `groupby().transform()`? When would you use each?
- Add a column `region_pct` showing each order's share of its region's total revenue.
