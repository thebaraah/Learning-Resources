# Week 2 — Exercise 2: Model Data with a Dataclass

**Concepts:** `@dataclass`, `__post_init__` validation, methods on data objects, `dataclasses.asdict`.

## Setup

No extra packages — just standard library.

```bash
python exercise.py
```

## Your task

Refactor the fragile dictionary into a `WeatherReading` dataclass that:

1. Has typed fields `city: str`, `temp_celsius: float`, `humidity: int`.
2. Rejects invalid humidity values (`humidity < 0` or `humidity > 100`) via `__post_init__` raising `ValueError`.
3. Has a method `is_hot()` that returns `True` if `temp_celsius > 30`.
4. Has a method `to_dict()` that converts the instance into a plain `dict` using `dataclasses.asdict`.

Then uncomment the assertion block at the bottom and confirm everything passes.

## Success criteria

- `WeatherReading(city="Amsterdam", temp_celsius=18.5, humidity=150)` raises `ValueError`.
- `WeatherReading(city="Amsterdam", temp_celsius=18.5, humidity=72).to_dict()` returns the expected dict.

## Stretch

Add a class method `from_dict(cls, data: dict)` that builds a `WeatherReading` from a dictionary (the inverse of `to_dict`).
