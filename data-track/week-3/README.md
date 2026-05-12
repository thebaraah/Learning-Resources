# HYF Data Track — Week 3 Practice Exercises

Six exercises that consolidate Week 3 (data ingestion, error handling, file formats, Pydantic validation, SQLite). Work through them in order: each one builds on patterns introduced in earlier chapters, and Exercise 6 wires every piece into a single end-to-end pipeline.

## Layout

Each exercise lives in its own subfolder so you can open a single Codespace and switch between them. The reference solution sits next to each starter under `solutions/` so you can compare side-by-side after you have tried.

| Folder | Topic | Concepts |
|---|---|---|
| [`exercise_1/`](exercise_1/) | Retry Function | `requests`, `try/except`, exponential backoff |
| [`exercise_2/`](exercise_2/) | Paginated API Fetch | Offset pagination, request pacing |
| [`exercise_3/`](exercise_3/) | Read and Normalize Formats | `csv.DictReader`, `json.load`, source-schema fan-in |
| [`exercise_4/`](exercise_4/) | Pydantic Validation | `BaseModel`, `Field`, `@field_validator`, batch validation |
| [`exercise_5/`](exercise_5/) | SQLite Writer | `sqlite3`, parameterised queries, `ON CONFLICT DO UPDATE` |
| [`exercise_6/`](exercise_6/) | Mini Pipeline (capstone) | Fetch → normalize → validate → upsert end-to-end |

```text
week-3/
├── exercise_1/
│   ├── exercise.py         # starter with TODOs
│   ├── README.md
│   ├── requirements.txt    # requests
│   └── solutions/
│       └── exercise.py     # reference answer with `# WHY ...` commentary
├── exercise_2/
│   └── …                   # paginated fetch with a local stub fixture
├── exercise_3/
│   ├── data/
│   │   ├── stations.csv
│   │   └── readings.json
│   └── …                   # normalize CSV + JSON into one shape
├── exercise_4/
│   └── …                   # Pydantic model + batch validation
├── exercise_5/
│   └── …                   # SQLite upsert (weather.db is gitignored)
└── exercise_6/
    └── …                   # end-to-end pipeline (capstone)
```

## Two ways to run

### A. Codespace (zero setup, runs in browser)

Spin up a single Codespace covering every data-track exercise:

> 💻 [Open in GitHub Codespaces](https://github.com/codespaces/new/HackYourFuture/Learning-Resources?devcontainer_path=.devcontainer%2Fdata-track%2Fdevcontainer.json)

The repo's `.devcontainer/data-track/` provisions Python 3.11 + ruff + Pylance + debugpy for every exercise folder. From the Codespace's Explorer, navigate into `data-track/week-3/exercise_N/` and run `pip install -r requirements.txt` once per exercise that ships one.

### B. Local clone (use your own VS Code)

```bash
git clone https://github.com/HackYourFuture/Learning-Resources.git
cd Learning-Resources/data-track/week-3
code .
```

Python 3.11+ required locally. Each exercise that needs extra packages ships its own `requirements.txt`; install with `pip install -r requirements.txt` from inside the folder.

## Reference solutions

Each `exercise_N/solutions/` folder holds the answer in-place: the same filename as the starter, filled in with the TODOs resolved and `# WHY ...:` comments under each non-obvious choice. The original `# TODO` lines are preserved so you can read the question and the answer side-by-side.

**Spoiler discipline.** The point of the reference solution is the commentary, not the code. Use it as a check after an honest attempt (or when you have been stuck for 10+ minutes); don't open it first. The folder is named `solutions/` and you have to deliberately navigate into it — that one extra click is the whole barrier and it is enough.

```bash
# After your attempt, diff against the reference:
diff exercise_1/exercise.py exercise_1/solutions/exercise.py
```
