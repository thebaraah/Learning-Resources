"""Exercise 4: Pydantic Validation.

Build a Pydantic model for a weather reading, add a custom validator, and
batch-validate a list of mixed-quality records.

Steps:
  1. Create a `WeatherReading(BaseModel)` with:
       station: str         (min_length=1)
       temperature_c: float (between -90 and 60)
       humidity_pct: int    (between 0 and 100)
       timestamp: str
  2. Add a `@field_validator("station")` that:
       - strips leading/trailing whitespace
       - converts to title case ("AARHUS" -> "Aarhus")
  3. Implement `validate_batch(records) -> (valid, errors)` that loops over
     records and uses error accumulation (try/except ValidationError) so a
     single bad row does not halt the batch.
  4. Run the test data at the bottom of this file.

Hint: import `BaseModel`, `Field`, `field_validator`, `ValidationError` from
`pydantic`. `@classmethod` is required immediately under `@field_validator`.
"""
from __future__ import annotations

# TODO: import BaseModel, Field, field_validator, ValidationError from pydantic


# TODO 1: define WeatherReading with the constraints above
# TODO 2: add the @field_validator that strips + title-cases the station name
class WeatherReading:
    """Replace this class with a Pydantic BaseModel."""


# TODO 3: implement validate_batch
def validate_batch(records: list[dict]) -> tuple[list[WeatherReading], list[dict]]:
    """Validate a batch, returning (valid_models, error_details)."""
    raise NotImplementedError


if __name__ == "__main__":
    test_data = [
        {"station": "copenhagen", "temperature_c": "18.5", "humidity_pct": "72", "timestamp": "2025-01-15T10:00"},
        {"station": "", "temperature_c": "abc", "humidity_pct": "150", "timestamp": "bad"},
        {"station": "  AARHUS  ", "temperature_c": "15.2", "humidity_pct": "65", "timestamp": "2025-01-15T11:00"},
    ]
    valid, errors = validate_batch(test_data)
    print(f"Valid: {len(valid)}, Errors: {len(errors)}")
    for model in valid:
        print(f"  ok: {model}")
    for err in errors:
        print(f"  fail: index={err['index']} fields={[e['loc'][0] for e in err['errors']]}")

    # Expected:
    #   Valid: 2, Errors: 1
    #   ok: station='Copenhagen' temperature_c=18.5 humidity_pct=72 timestamp='2025-01-15T10:00'
    #   ok: station='Aarhus' temperature_c=15.2 humidity_pct=65 timestamp='2025-01-15T11:00'
    #   fail: index=1 fields=['station', 'temperature_c', 'humidity_pct']
