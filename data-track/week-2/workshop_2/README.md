# Workshop 2 Starter: Composable Transforms + Dataclasses

Three parts:

- **Part A (5 min):** discuss the function-vs-class snippets in `function_vs_class.py`. Which one *needs* to be a class? Why?
- **Part B (10 min):** define `Transaction` with `__post_init__` validation in `models.py`.
- **Part C (10 min):** wire the chain in `pipeline.py` and print the row count after each step.

The decision rule: **data + config → classes; logic + transforms → functions.**

Setup:

```bash
pip install python-dotenv
# data/sales.csv is already provided in the data/ folder
python pipeline.py
```
