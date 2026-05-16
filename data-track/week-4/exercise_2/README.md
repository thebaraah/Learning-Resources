# Exercise 2: Filtering and Sorting

**Concepts:** Boolean masks, `loc`, sorting.

## Setup

The setup block at the top of `exercise.py` creates and cleans the `orders` DataFrame for you. No separate file needed.

## Task

Work through the three TODOs:

1. Filter orders where `region` is `NL` **and** `amount` is greater than `80`. Use `&` to combine conditions (not `and`).
2. Sort the filtered result by `amount` descending using `sort_values()`.
3. Add a boolean column `is_big_order` to the original `orders` DataFrame: `True` where `amount >= 150`.

## Success criteria

- `nl_big_sorted` contains exactly 1 row (order_id 1, amount 120).
- `orders['is_big_order']` has `True` only for order_id 4 (amount 200).

## Stretch

- Try using `.loc[]` to select only the `region` and `amount` columns from `nl_big_sorted`.
- What happens if you use `and` instead of `&` between two boolean conditions? Why does pandas require `&`?
