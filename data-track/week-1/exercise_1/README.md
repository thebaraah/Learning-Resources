# Week 1: Setup, Tools, CLI and Git

[📖 View on Notion](https://hub.hackyourfuture.nl/Practice-2af50f64ffc981479b34e4e4ad74fbc8?pvs=74)

# Exercise 1: The Temperature Logger

**Concepts:** Variables, Functions, Type Hinting, Logging.

You are building a small weather station script. Your task is to write a function that converts Celsius to Fahrenheit, but it must be “production-ready”.

**Instructions:**

1. Import the `logging` module and configure it to level `INFO`.
1. Write a function called `convert_c_to_f`.
1. **Type Hinting:** The function should accept a `float` and return a `float`.
1. Inside the function, calculate the result (`(celsius * 9/5) + 32`).
1. **Logging:** Before returning the value, log an `info` message: `"Converting {celsius}°C to {fahrenheit}°F"`.
1. Call the function with three different values (e.g., 0, 25, 100).