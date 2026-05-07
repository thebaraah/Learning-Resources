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

```text
week-2/
├── exercise_1/
│   ├── starter.py       # starter with TODOs
│   ├── README.md        # what to do
│   └── solutions/
│       └── starter.py   # reference answer with `# WHY …` commentary
├── exercise_2/
│   └── …
└── exercise_5/
```

## Two ways to run

### A. Codespace (zero setup, runs in browser)

Spin up a single Codespace covering all data-track exercises:

> 💻 [Open in GitHub Codespaces](https://github.com/codespaces/new/HackYourFuture/Learning-Resources?folder=data-track)

The repo's `data-track/.devcontainer/` provisions Python 3.11 + the VS Code Python extensions for every exercise folder. From the Codespace's Explorer, navigate into `data-track/week-2/exercise_N/`.

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
