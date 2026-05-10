# Workshop 1 Starter: Config + Separation of Concerns

Refactor the disaster script using:

- **Part A (10 min):** extract config to `.env` + `config.py`. Success: change `.env` only and the script picks up the new path with no code edit.
- **Part B (15 min):** extract pure transform functions (`clean_names`, `calculate_revenue`) that return new lists. Success: `raw[0]` prints unchanged after the full chain.

Setup:

```bash
pip install python-dotenv
cp .env.example .env
mkdir -p output
# data/sales.csv is already provided in the data/ folder
python pipeline.py
```

Files:

- `.env.example`: template, copy to `.env`.
- `config.py`: TODO stubs.
- `pipeline.py`: has the I/O scaffolding; you fill in the transforms.
