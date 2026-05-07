# Week 1: Setup, Tools, CLI and Git

[📖 View on Notion](https://hub.hackyourfuture.nl/Practice-2af50f64ffc981479b34e4e4ad74fbc8?pvs=74)

# Exercise 5: The File Ingestor

**Concepts:** File I/O, Strings, Context Managers (`with`).

A big part of Data Engineering is reading data from files. Let’s practice reading a raw text file and processing it.

**Instructions:**

1. Create a text file named `raw_data.txt` in your folder. Add these lines:

```plain text
amsterdam
rotterdam
the hague
utrecht
```

1. Create a python script `assignment_6.py`.
1. Use the `with open(...)` pattern to **read** the `raw_data.txt` file.
1. Loop through the lines and **capitalize** each city name (e.g., “Amsterdam”).
1. Store the cleaned names in a list.
1. Use `with open(...)` again to **write** the cleaned names into a new file called `processed_data.txt`.
1. Check your folder to see if the new file was created!
1. **Interactive Version:** If you want to try this without local files, use the widget.