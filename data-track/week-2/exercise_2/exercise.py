"""Exercise 2: Model Data with a Dataclass.

The dictionary below is fragile: a typo like `reading["temprature"]`
goes unnoticed until runtime. Refactor it into a WeatherReading
dataclass with validation and behaviour.
"""

# BAD: fragile dictionary
reading = {
    "city": "Amsterdam",
    "temp_celsius": 18.5,
    "humidity": 72,
}


# TODO 1: Create a WeatherReading dataclass with three fields:
#   - city: str
#   - temp_celsius: float
#   - humidity: int
#
# TODO 2: Add a __post_init__ method that raises ValueError if humidity
# is outside 0..100. Hint: a humidity of 150 should fail loudly.
#
# TODO 3: Add a method `is_hot(self) -> bool` returning True if
# temp_celsius > 30.
#
# TODO 4: Add a method `to_dict(self) -> dict` using dataclasses.asdict
# to convert the instance back to a plain dict for serialisation.


# Once you have the dataclass, replace the dictionary above with an
# instance and uncomment the asserts below.

# r = WeatherReading(city="Amsterdam", temp_celsius=18.5, humidity=72)
# assert r.city == "Amsterdam"
# assert r.is_hot() is False
# assert r.to_dict() == {"city": "Amsterdam", "temp_celsius": 18.5, "humidity": 72}
#
# try:
#     WeatherReading(city="Amsterdam", temp_celsius=18.5, humidity=150)
# except ValueError as exc:
#     print(f"Correctly rejected: {exc}")
# else:
#     raise AssertionError("Expected ValueError for humidity=150")

# Expected once your dataclass is in place:
# Correctly rejected: humidity must be between 0 and 100
print("Replace the asserts above with your dataclass implementation.")
