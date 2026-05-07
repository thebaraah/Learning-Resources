# Week 1: Setup, Tools, CLI and Git

[📖 View on Notion](https://hub.hackyourfuture.nl/Practice-2af50f64ffc981479b34e4e4ad74fbc8?pvs=74)

# Exercise 2: The Data Cleaner

**Concepts:** Lists, Loops, Conditionals, Debugging.

You have received a list of user ages from a database, but the data is dirty. Some values are strings, some are numbers, and some are negative (impossible!).

**The Buggy Code:**
Copy this into `exercise_2.py`. It currently crashes.

```python
ages = [25, 30, "40", "not_available", 20, -5]

def calculate_average_age(age_list):
    total = 0
    count = 0
    for age in age_list:
        total += age
        count += 1

    return total / count

print(calculate_average_age(ages))
```

**Instructions:**

1. Run the code and read the **Traceback**. What kind of error is it?
1. Use the **VS Code Debugger** to step through the loop. Find which value causes the crash.
1. Modify the loop to fix the code:

- If the value is a string that represents a number (like `"40"`), convert it to an int.
- If the value is not a number (like `"not_available"`), skip it.
- If the value is negative, skip it.

1. Print the final correct average.