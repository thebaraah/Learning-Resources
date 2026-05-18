import tempfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # headless backend: no display required
import matplotlib.pyplot as plt
import pandas as pd


def section_1_quick_plots():
    print("--- Section: Quick Plots with DataFrame.plot ---")
    sales = pd.DataFrame(
        {
            "date": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
            "amount": [120, 90, 150],
        }
    ).sort_values("date")

    ax = sales.plot(x="date", y="amount", kind="line", title="Daily revenue")
    print(f"Line chart created, type: {type(ax).__name__}")
    plt.close()

    # kind="bar" requires string x-axis (bar charts treat each tick as a category)
    sales_str = sales.copy()
    sales_str["date"] = sales_str["date"].dt.strftime("%Y-%m-%d")
    ax_bar = sales_str.plot(x="date", y="amount", kind="bar", title="Daily revenue (bar)")
    print(f"Bar chart created, type: {type(ax_bar).__name__}")
    plt.close()


def section_2_group_then_plot():
    print("\n--- Section: Group Then Plot ---")
    orders = pd.DataFrame(
        {
            "region": ["NL", "NL", "BE", "DE", "BE"],
            "amount": [120, 80, 200, 50, 90],
        }
    )
    # Aggregating before plotting ensures one bar per region
    by_region = orders.groupby("region", as_index=False)["amount"].sum()
    ax = by_region.plot(x="region", y="amount", kind="bar", title="Revenue by region")
    print("Aggregated before plotting.")
    print(by_region)
    plt.close()


def section_3_matplotlib_control():
    print("\n--- Section: Matplotlib for More Control ---")
    sales = pd.DataFrame(
        {
            "date": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
            "amount": [120, 90, 150],
        }
    ).sort_values("date")

    with tempfile.TemporaryDirectory() as tmp:
        output_path = Path(tmp) / "daily_revenue.png"
        ax = sales.plot(x="date", y="amount", kind="line", figsize=(6, 3))
        ax.set_xlabel("Date")
        ax.set_ylabel("Revenue")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        assert output_path.exists()
        size = output_path.stat().st_size
        print(f"Chart saved to temp file ({size} bytes). File exists: {output_path.exists()}")


def section_4_histogram():
    print("\n--- Section: Histogram for Distributions ---")
    import random
    random.seed(42)
    orders = pd.DataFrame({"amount": [random.randint(10, 500) for _ in range(100)]})
    ax = orders["amount"].plot(kind="hist", bins=10, title="Order amount distribution")
    print(f"Histogram created with 100 orders. Axes type: {type(ax).__name__}")
    plt.close()


if __name__ == "__main__":
    section_1_quick_plots()
    section_2_group_then_plot()
    section_3_matplotlib_control()
    section_4_histogram()
