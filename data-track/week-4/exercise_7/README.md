# Exercise 7: Visualize Revenue

**Concepts:** `groupby` + `plot`, `savefig`, headless backend.

## Setup

The setup block in `exercise.py` creates the `orders` DataFrame and the `output/` folder. No extra setup needed beyond installing the packages.

## Task

1. Group `orders` by `region` and sum `amount`. Plot the result as a bar chart using `.plot(kind='bar')`.
2. Add axis labels (`Region` on x, `Total Revenue (€)` on y) and a title (`Revenue by Region`).
3. Call `plt.tight_layout()` then save the figure to `output/revenue_by_region.png`. Confirm the file exists with `Path("output/revenue_by_region.png").exists()`.

## Success criteria

- `output/revenue_by_region.png` is created.
- `Path("output/revenue_by_region.png").exists()` prints `True`.
- The chart has three bars: one per region (BE, DE, NL).

## Note

`matplotlib.use("Agg")` must be called **before** importing `matplotlib.pyplot`. The `Agg` backend renders to a file without opening a display window, which is required in Codespaces and any headless server environment.

## Stretch

- Sort the regions by revenue before plotting so the bars go from highest to lowest.
- Try `kind='barh'` (horizontal bar chart). When is a horizontal bar chart preferable?
