# Deep Dive (Week 2 §7)

Three runnable demos used in the in-class concept deep-dive:

- `mutation_demo.py`: Gotcha #1: how in-place mutation corrupts the caller's data, and the `{**row, ...}` fix.
- `mutable_default_trap.py`: Gotcha #2: how `tags: list = []` shares state across calls in functions, and crashes loudly in dataclasses (the fix: `field(default_factory=list)`).
- `test_transforms.py` + `transforms.py`: pure-function tests that need no CSV file.

```bash
pip install pytest
python mutation_demo.py
python mutable_default_trap.py
pytest -v test_transforms.py
```
