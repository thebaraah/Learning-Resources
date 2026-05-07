"""Reference solution (in-place over the starter).

Each `# 1.`, `# 4.`, `# 5.`, `# 6.` comment below is the original TODO
from the starter. The code immediately under it is the answer, with
`# WHY ...:` notes explaining non-obvious choices.

Teaches: production-ready function shape — type hints + structured
logging instead of print(). The whole exercise is one tiny function,
but it carries every habit a junior data engineer needs on day one.
"""
import logging

# 1. Configure logging to level INFO
# WHY level=INFO: INFO + WARNING + ERROR are visible by default;
# DEBUG is hidden unless explicitly enabled. INFO is the right
# baseline for a normal-looking pipeline — loud enough to confirm it
# ran, quiet enough not to bury real warnings.
logging.basicConfig(level=logging.INFO)


def convert_c_to_f(celsius: float) -> float:
    """
    Converts Celsius to Fahrenheit.
    """
    # 4. Calculate the result: (celsius * 9/5) + 32
    fahrenheit = (celsius * 9 / 5) + 32

    # 5. Log an info message: "Converting {celsius}°C to {fahrenheit}°F"
    # WHY logging.info BEFORE returning: capture the conversion every
    # time the function is called so an operator can audit the
    # pipeline's behaviour after the fact. Returning silently would
    # discard that signal — exactly the "silent failure" trap from
    # Gotcha #8 (print vs logging).
    logging.info(f"Converting {celsius}°C to {fahrenheit}°F")
    return fahrenheit


# 6. Call the function with three different values (e.g., 0, 25, 100)
# WHY 0 / 25 / 100: freezing point, room temperature, boiling point.
# Quick visual check that each conversion produces a sensible number
# (32, 77, 212).
convert_c_to_f(0)
convert_c_to_f(25)
convert_c_to_f(100)
