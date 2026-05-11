# Workshop 2 Starter: Composable Transforms + Dataclasses

Four parts:

- **Part A (5 min):** discuss the function-vs-class snippets in `function_vs_class.py`. Which one *needs* to be a class? Why?
- **Part B (10 min):** define `Transaction` with `@dataclass` and `__post_init__` validation in `models.py`. Note: `@dataclass` is a decorator — a function applied to your class to auto-generate `__init__`, `__repr__`, and more.
- **Part C (10 min):** wire the chain in `pipeline.py` and print the row count after each step.
- **Part D (10 min):** write three pytest tests in `test_pipeline.py` — one each for `clean_names`, `remove_invalid`, and `Transaction` validation.

The decision rule: **data + config → classes; logic + transforms → functions.**

Setup:

```bash
pip install python-dotenv pytest
# data/sales.csv is already provided in the data/ folder
python pipeline.py
pytest test_pipeline.py -v
```
