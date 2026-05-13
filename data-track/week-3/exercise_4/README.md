# Exercise 4: Pydantic Validation

Build a model, add a custom validator, and batch-validate dirty data.

## Setup

```bash
pip install -r requirements.txt
```

## The task

1. Define a `WeatherReading(BaseModel)` with:
   - `station: str` (`min_length=1`)
   - `temperature_c: float` (`ge=-90, le=60`)
   - `humidity_pct: int` (`ge=0, le=100`)
   - `timestamp: str`
2. Add a `@field_validator("station")` (with `@classmethod` on the line below) that strips whitespace and converts to `.title()` case.
3. Implement `validate_batch(records)` that:
   - Loops over the input list.
   - Tries to instantiate `WeatherReading(**record)` inside a `try/except`.
   - On success, appends to `valid`. On `ValidationError`, appends to `errors` as `{"index": i, "record": record, "errors": e.errors()}`.
   - Returns `(valid, errors)`.

## Success criteria

Running the script prints:

```text
Valid: 2, Errors: 1
  ok: station='Copenhagen' temperature_c=18.5 humidity_pct=72 timestamp='2025-01-15T10:00'
  ok: station='Aarhus' temperature_c=15.2 humidity_pct=65 timestamp='2025-01-15T11:00'
  fail: index=1 fields=['station', 'temperature_c', 'humidity_pct']
```

Both passing rows are title-cased. The failing row reports which fields broke.

## Stretch

- Add a `@field_validator("timestamp")` that requires either `T` or a space between date and time.
- Add a `humidity_warning: str | None = None` field that the validator fills in when humidity is over 95 ("near saturation").
