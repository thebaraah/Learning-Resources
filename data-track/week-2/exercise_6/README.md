# Exercise 6: OOP vs Functional — Spot the State

**Concepts:** OOP vs Functional (Ch4)

Three pipeline components, each implemented as a class. For each one, decide:

- **Keep as a class?** Does it hold state that methods share via `self`?
- **Refactor to a plain function?** Is it just input → output with nothing stored?

Then refactor the ones that should not be classes.

## Instructions

Open `exercise.py`. Read each snippet, then:

1. Write a comment above each class: `# KEEP AS CLASS` or `# REFACTOR TO FUNCTION`
2. For each one marked `# REFACTOR TO FUNCTION`, rewrite it as a plain function below the original.
3. Run the short checks at the bottom of the file to verify your refactored functions produce the same output.

**Success criteria:** Both refactored functions produce the same result as the original class methods. The one correct class is left as-is.

## Time

15 minutes.

## Reference solution

`solutions/exercise.py` — with `# WHY` notes explaining each decision.
