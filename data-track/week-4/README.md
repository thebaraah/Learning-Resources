# HYF Data Track — Week 4 Practice Exercises

Seven exercises that consolidate Week 4 (pandas fundamentals: EDA, filtering, groupby, joins, reshaping, string/date processing, and visualisation). Work through them in order: Exercises 2-5 build on the `orders` DataFrame you create in Exercise 1.

## Layout

Each exercise lives in its own subfolder so you can open a single Codespace and switch between them. The reference solution sits next to each starter under `solutions/` so you can compare side-by-side after you have tried.

| Folder | Topic | Concepts |
|---|---|---|
| [`exercise_1/`](exercise_1/) | Quick EDA on Orders | `info()`, `describe()`, missing values, `fillna()` |
| [`exercise_2/`](exercise_2/) | Filtering and Sorting | Boolean masks, `loc`, `sort_values` |
| [`exercise_3/`](exercise_3/) | Grouping and Aggregation | `groupby`, `agg`, `transform` |
| [`exercise_4/`](exercise_4/) | Joining Two Tables | `merge`, join types |
| [`exercise_5/`](exercise_5/) | Reshape and Export | `pivot_table`, CSV, Parquet |
| [`exercise_6/`](exercise_6/) | Strings and Dates | `.str` accessor, `pd.to_datetime`, `.dt` accessor |
| [`exercise_7/`](exercise_7/) | Visualize Revenue | `groupby` + `plot`, `savefig`, headless backend |

```text
week-4/
├── exercise_1/
│   ├── exercise.py        # starter with TODOs
│   ├── README.md          # instructions and success criteria
│   ├── requirements.txt   # pandas
│   └── solutions/
│       └── exercise.py    # reference answer with # WHY commentary
├── exercise_2/
│   └── …
├── exercise_3/
│   └── …
├── exercise_4/
│   └── …
├── exercise_5/
│   ├── exercise.py
│   ├── requirements.txt   # pandas + pyarrow
│   └── solutions/
│       └── exercise.py
├── exercise_6/
│   └── …
└── exercise_7/
    ├── exercise.py
    ├── requirements.txt   # pandas + matplotlib
    └── solutions/
        └── exercise.py
```

## Two ways to run

### A. Codespace (zero setup, runs in browser)

Spin up a single Codespace covering all data-track exercises:

> 💻 [Open in GitHub Codespaces](https://github.com/codespaces/new/HackYourFuture/Learning-Resources?devcontainer_path=.devcontainer%2Fdata-track%2Fdevcontainer.json)

The repo's `.devcontainer/data-track/` provisions Python 3.11 + ruff + Pylance + debugpy for every exercise folder. From the Codespace's Explorer, navigate into `data-track/week-4/exercise_N/`.

### B. Local clone (use your own VS Code)

```bash
git clone https://github.com/HackYourFuture/Learning-Resources.git
cd Learning-Resources/data-track/week-4
code .
```

Python 3.11+ required locally. Each exercise that needs extra packages ships its own `requirements.txt`; install with `pip install -r requirements.txt` from inside the folder.

## Reference solutions

Each `exercise_N/solutions/` folder holds the answer in-place: the same filenames as the starter, filled in with the TODOs resolved and `# WHY …:` comments under each non-obvious choice. The original `# TODO` lines are preserved so you can read the question and the answer side-by-side.

**Spoiler discipline.** The point of the reference solution is the commentary, not the code. Use it as a check after an honest attempt (or when you have been stuck for 10+ minutes); don't open it first. The folder is named `solutions/` and you have to deliberately navigate into it — that one extra click is the whole barrier and it is enough.

When you do open a solution, read the `# WHY` comments before reading the code. The point is to learn why a particular shape was chosen, not to memorise the shape itself.
