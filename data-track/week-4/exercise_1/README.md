# Exercise 1: Quick EDA on Orders

**Concepts:** DataFrame creation, `info()`, `describe()`, missing values.

## Setup

Use the Codespace at the top of the week-4 README for zero setup. If running locally, run `pip install -r requirements.txt` from inside this folder first.

## Task

You have a small CSV embedded in the script. Work through the three TODOs:

1. Call `orders.info()` and `orders.describe()`. Print both so you can read the output.
2. Count missing values per column with `.isnull().sum()`.
3. Fill missing `amount` values with `0` using `fillna()`.

## Success criteria

- `orders.info()` shows `amount` as `float64` with 4 non-null entries before the fill.
- `.isnull().sum()` shows `amount` has 1 missing value.
- After `fillna(0)`, `.isnull().sum()` on `amount` returns `0`.

## Stretch

- Why does pandas infer `float64` for `amount` when most values look like integers?
- What would happen if you used `fillna(orders['amount'].mean())` instead of `fillna(0)`?

## Note

Each exercise is self-contained: the same sample data is embedded in every starter file. You do not need to run this exercise before starting Exercise 2.
