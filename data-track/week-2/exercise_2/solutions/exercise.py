"""Reference solution (in-place over the starter)."""
from dataclasses import asdict, dataclass


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
@dataclass
class WeatherReading:
    """A weather observation. Validates humidity at construction time."""

    city: str
    temp_celsius: float
    humidity: int

    # WHY __post_init__: @dataclass auto-generates __init__ from the
    # field declarations above. Adding our own __init__ would override
    # that and lose the auto-generation. __post_init__ is the documented
    # hook that runs *after* the generated __init__ finishes, exactly
    # for validation like this.
    def __post_init__(self) -> None:
        if not 0 <= self.humidity <= 100:
            raise ValueError(
                f"humidity must be between 0 and 100, got {self.humidity}"
            )

    # WHY a method instead of a standalone is_hot(reading) function:
    # the rule ("hot" means temp_celsius > 30) is intrinsic to the
    # WeatherReading type. Putting it on the class keeps the rule and
    # the data it operates on in one place. Not every helper deserves
    # this treatment — this one does because the threshold is part of
    # what 'a weather reading' means in this domain.
    def is_hot(self) -> bool:
        return self.temp_celsius > 30

    # WHY asdict instead of vars() or __dict__: asdict recursively
    # converts nested dataclasses too, and it explicitly returns a plain
    # dict that downstream code (json.dumps, csv.DictWriter, requests)
    # can consume.
    def to_dict(self) -> dict:
        return asdict(self)


# Once you have the dataclass, replace the dictionary above with an
# instance and uncomment the asserts below.
r = WeatherReading(city="Amsterdam", temp_celsius=18.5, humidity=72)
assert r.city == "Amsterdam"
assert r.is_hot() is False
assert r.to_dict() == {"city": "Amsterdam", "temp_celsius": 18.5, "humidity": 72}

try:
    WeatherReading(city="Amsterdam", temp_celsius=18.5, humidity=150)
except ValueError as exc:
    print(f"Correctly rejected: {exc}")
else:
    raise AssertionError("Expected ValueError for humidity=150")

# Expected once your dataclass is in place:
# Correctly rejected: humidity must be between 0 and 100, got 150
