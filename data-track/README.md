# HYF Data Track — Practice Exercises

Reference exercises that accompany the [HYF Data Track curriculum](https://www.notion.so/hackyourfuture/Data-track). Each week mirrors the chapters of the same week on Notion: Week 1 is Python foundations, Week 2 is structuring data pipelines, and so on.

Curriculum chapters link directly into specific exercise folders here. You don't need to clone anything to read the chapter — but to *do* the practice, open a Codespace (zero setup) or clone the repo locally.

## Open the workspace once

A single Codespace covers every week's exercises:

> 💻 [Open in GitHub Codespaces](https://github.com/codespaces/new/HackYourFuture/Learning-Resources?devcontainer_path=.devcontainer%2Fdata-track%2Fdevcontainer.json)

The Codespace opens directly in `data-track/` with Python 3.11 + the VS Code Python extensions provisioned via [`.devcontainer/data-track/devcontainer.json`](../.devcontainer/data-track/devcontainer.json). Navigate into whichever week and exercise you're working on from the Explorer.

To clone instead:

```bash
git clone https://github.com/HackYourFuture/Learning-Resources.git
cd Learning-Resources/data-track
```

## Weeks

| Week | Folder | Topic |
|---|---|---|
| 1 | [`week-1/`](week-1/) | Python Foundations |
| 2 | [`week-2/`](week-2/) | Structuring Data Pipelines |
| 3 onwards | (pending migration) | |

## Layout

Each week is a flat list of `exercise_N/` folders. Each exercise carries its starter (`exercise.py` or similar) plus a `solutions/` subfolder with the reference answer. The `solutions/` folder is right next to the starter so you can diff against it cheaply once you have tried — but you have to deliberately open the folder, which is the spoiler barrier we want.

```text
.devcontainer/
└── data-track/
    └── devcontainer.json   (Codespaces config: Python 3.11 + ruff + Pylance + debugpy)

data-track/
├── README.md               (you are here)
├── week-1/
│   ├── README.md           (Week 1 exercise overview)
│   ├── exercise_1/
│   │   ├── exercise.py
│   │   ├── README.md
│   │   └── solutions/
│   └── …
└── week-2/
    └── …
```

## Spoiler discipline

The chapter you are reading on Notion will tell you to attempt an exercise on your own first. The `solutions/` folder is the answer key: don't open it until you have tried. After your attempt, read the `# WHY …:` comments under each TODO before you read the code itself — the reasoning matters more than the syntax.
