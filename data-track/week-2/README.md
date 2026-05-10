# HYF Data Track — Week 2 Practice Exercises

Five small exercises that consolidate Week 2 (configuration & secrets, dataclasses, separation of concerns, pytest, refactoring). Work through them in order: each one builds on patterns introduced in earlier chapters.

## Layout

Each exercise lives in its own subfolder so you can open a single Codespace and switch between them. The reference solution sits next to each starter under `solutions/` so you can compare side-by-side after you have tried.

| Folder | Topic | Concepts |
|---|---|---|
| [`exercise_1/`](exercise_1/) | Move Secrets to .env | `python-dotenv`, `os.environ`, `config.py` |
| [`exercise_2/`](exercise_2/) | Model Data with a Dataclass | `@dataclass`, `__post_init__` validation, methods |
| [`exercise_3/`](exercise_3/) | Separate I/O from Logic | Pure functions, dependency injection, orchestration |
| [`exercise_4/`](exercise_4/) | Write Tests with Pytest | `pytest`, fixtures, parametrize |
| [`exercise_5/`](exercise_5/) | Refactor a "god function" | Combine all five concepts on one messy script |

### Session Workshops & Demos (Live)

| Folder | Topic | Concepts |
|---|---|---|
| [`disaster_script/`](disaster_script/) | The Disaster Script | What's wrong with this code? |
| [`workshop_1/`](workshop_1/) | Workshop 1: Config + Separation | `.env`, `config.py`, pure functions |
| [`workshop_2/`](workshop_2/) | Workshop 2: Composable + Dataclasses | `@dataclass`, `__post_init__`, pipelines |
| [`demos/`](demos/) | Concept Deep-dives | Mutation, mutable defaults, pure tests |
| [`ruff_practice/`](ruff_practice/) | Ruff Practice | Fixing a messy file with `ruff check` |

```text
week-2/
├── exercise_1/
│   ├── exercise.py        # starter with TODOs
│   ├── .env.example       # copy to .env (gitignored) before running
│   ├── README.md          # what to do
│   └── solutions/
│       └── exercise.py    # reference answer with `# WHY …` commentary
├── exercise_2/
│   └── …
├── exercise_4/            # tests-focused: starter is `test_sales.py`
│   ├── sales.py
│   ├── test_sales.py
│   └── solutions/
│       └── test_sales.py
├── exercise_5/            # capstone: solution is a multi-file refactor
│   ├── exercise.py
│   └── solutions/
│       ├── main.py
│       ├── models.py
│       ├── transforms.py
│       └── io_layer.py
├── workshop_1/            # live workshop: config + separation
├── workshop_2/            # live workshop: composable + dataclasses
├── disaster_script/       # live demo: the disaster script
└── demos/                 # live demo: deep dives
```

## Two ways to run

### A. Codespace (zero setup, runs in browser)

Spin up a single Codespace covering all data-track exercises:

> 💻 [Open in GitHub Codespaces](https://github.com/codespaces/new/HackYourFuture/Learning-Resources?devcontainer_path=.devcontainer%2Fdata-track%2Fdevcontainer.json)

The repo's `.devcontainer/data-track/` provisions Python 3.11 + ruff + Pylance + debugpy for every exercise folder. From the Codespace's Explorer, navigate into `data-track/week-2/exercise_N/`.

### B. Local clone (use your own VS Code)

```bash
git clone https://github.com/HackYourFuture/Learning-Resources.git
cd Learning-Resources/data-track/week-2
code .
```

Python 3.11+ required locally. Each exercise that needs extra packages ships its own `requirements.txt`; install with `pip install -r requirements.txt` from inside the folder.

## Reference solutions

Each `exercise_N/solutions/` folder holds the answer in-place: the same filenames as the starter, filled in with the TODOs resolved and `# WHY …:` comments under each non-obvious choice. The original `# TODO` lines are preserved so you can read the question and the answer side-by-side.

**Spoiler discipline.** The point of the reference solution is the commentary, not the code. Use it as a check after an honest attempt (or when you have been stuck for 10+ minutes); don't open it first. The folder is named `solutions/` and you have to deliberately navigate into it — that one extra click is the whole barrier and it is enough.

When you do open a solution, read the `# WHY` comments before reading the code. The point is to learn why a particular shape was chosen, not to memorise the shape itself.
