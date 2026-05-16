# Exercise 6: Strings and Dates

**Concepts:** `.str` accessor, `pd.to_datetime`, `.dt` accessor.

## Setup

The setup block in `exercise.py` extends `orders` with a mixed-case `email` column and converts `order_date` to datetime.

## Task

1. Normalise `email` to lowercase with no leading/trailing whitespace using `.str.strip()` then `.str.lower()`. Both methods skip `NaN` values by default, so missing emails stay as `NaN`.
2. Extract `year` and `month` from `order_date` as new integer columns using `.dt.year` and `.dt.month`.
3. Filter to orders placed in January 2024 using `.dt.month` and `.dt.year`.

## Success criteria

- `orders['email']` has `bob@example.com` (lowercase) for order_id 2.
- `orders['month']` contains only `1` (all dates are in January).
- `jan_orders` has all 5 rows (every order is in January 2024).

## Stretch

- What does `.str.lower()` return for a `None` / `NaN` value? Verify by printing `orders['email'].isnull()` after the normalisation step.
- Filter to orders placed on or after January 3 using `.dt.date` or comparison with a `pd.Timestamp`.
