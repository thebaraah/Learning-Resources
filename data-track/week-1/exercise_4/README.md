# Week 1: Setup, Tools, CLI and Git

[📖 View on Notion](https://hub.hackyourfuture.nl/Practice-2af50f64ffc981479b34e4e4ad74fbc8?pvs=74)

# Exercise 4: Grade Processor (Final Boss)

**Concepts:** Dictionaries, Type Hinting, Logging, Complex Logic.

Combine everything! You need to process student grades.

**Instructions:**

1. Create a dictionary representing a student:

```python
student = {"name": "Alice", "grades": [85, 90, 78]}
```

1. Write a function `process_student(student_data: dict) -> None`.
1. Configure `logging` to show timestamps.
1. Inside the function:

- Log an `INFO` message: “Processing grades for [Name]”.
- Calculate the average grade.
- If average > 80, log `INFO`: “Grade A”.
- If average > 60, log `INFO`: “Grade B”.
- Otherwise, log `WARNING`: “Student requires assistance”.

1. Call the function with Alice’s data.