# HYF Data Track — Week 1 Practice Exercises

Six small exercises that consolidate Week 1 (variables, functions, type hints, logging, debugging, file I/O, CLI). Pick the ones that match what felt shaky on a first read of the chapter; you can do them in any order.

## Layout

Each exercise lives in its own subfolder so you can open a single Codespace and switch between them. The reference solution sits next to each starter under `solutions/` so you can compare side-by-side after you have tried.

| Folder | Topic | Concepts |
|---|---|---|
| [`exercise_1/`](exercise_1/) | The Temperature Logger | Variables, functions, type hints, logging |
| [`exercise_2/`](exercise_2/) | The Data Cleaner | Lists, loops, conditionals, debugging |
| [`exercise_3/`](exercise_3/) | The Precision Trap | Floating-point math, debugger usage |
| [`exercise_4/`](exercise_4/) | Grade Processor | Dictionaries, type hints, logging, branching |
| [`exercise_5/`](exercise_5/) | The File Ingestor | File I/O, context managers, strings |
| [`exercise_6/`](exercise_6/) | The Pipeline CLI | argparse, logging levels, pathlib |

```text
week-1/
├── exercise_1/
│   ├── exercise.py        # starter with TODOs
│   ├── README.md          # what to do
│   └── solutions/
│       └── exercise.py    # reference answer with `# WHY …` commentary
├── exercise_2/
│   └── …
└── exercise_6/
```

## Two ways to run

### A. Codespace (zero setup, runs in browser)

Spin up a single Codespace covering all data-track exercises:

> 💻 [Open in GitHub Codespaces](https://github.com/codespaces/new/HackYourFuture/Learning-Resources?devcontainer_path=.devcontainer%2Fdata-track%2Fdevcontainer.json)

The repo's `.devcontainer/data-track/` provisions Python 3.11 + ruff + Pylance + debugpy for every exercise folder. From the Codespace's Explorer, navigate into `data-track/week-1/exercise_N/`.

### B. Local clone (use your own VS Code)

```bash
git clone https://github.com/HackYourFuture/Learning-Resources.git
cd Learning-Resources/data-track/week-1
code .
```

Python 3.11+ required locally. If an exercise ships a `requirements.txt`, run `pip install -r requirements.txt` inside that subfolder first.

## Reset a single exercise

If you've made a mess of one folder and want a clean slate, reset only that subfolder rather than wiping the whole workspace:

```bash
git checkout -- exercise_3/
```

That gives you the original starter files for Exercise 3 without touching your work in the other folders.

## Reference solutions

Each `exercise_N/solutions/` folder holds the answer in-place: the same filename as the starter (e.g. `exercise.py`) with the TODO blocks filled in and `# WHY …:` comments under each non-obvious choice.

**Spoiler discipline.** The point of the reference solution is the commentary, not the code. Use it as a check after an honest attempt (or when you have been stuck for 30+ minutes); don't open it first. The folder is named `solutions/` and you have to deliberately navigate into it — that one extra click is the whole barrier and it is enough.

When you do open a solution, read the `# WHY` comments before reading the code. The point is to learn why a particular shape was chosen, not to memorise the shape itself.
