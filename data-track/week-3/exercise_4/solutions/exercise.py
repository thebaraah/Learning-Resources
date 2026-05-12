"""Exercise 4 — Reference solution.

Read the `# WHY ...:` notes, not the code.
"""
from __future__ import annotations

from pydantic import BaseModel, Field, ValidationError, field_validator


# TODO 1: define WeatherReading with the constraints above
# TODO 2: add the @field_validator that strips + title-cases the station name
class WeatherReading(BaseModel):
    station: str = Field(min_length=1)
    temperature_c: float = Field(ge=-90, le=60)
    humidity_pct: int = Field(ge=0, le=100)
    timestamp: str

    @field_validator("station")
    @classmethod
    def normalize_station(cls, v: str) -> str:
        # WHY strip THEN title-case: "  AARHUS  ".strip().title() == "Aarhus".
        # Doing it in reverse would keep the leading/trailing whitespace,
        # which silently fails the `min_length=1` check on an all-whitespace
        # input later in the run.
        cleaned = v.strip()
        if not cleaned:
            # WHY raise here too: Field(min_length=1) catches an empty string
            # input, but not an "all whitespace" input — the validator runs
            # AFTER constraints have already cleared the original value.
            raise ValueError("station cannot be blank or whitespace-only")
        return cleaned.title()


# TODO 3: implement validate_batch
def validate_batch(records: list[dict]) -> tuple[list[WeatherReading], list[dict]]:
    """Validate a batch, returning (valid_models, error_details)."""
    valid: list[WeatherReading] = []
    errors: list[dict] = []
    # WHY error accumulation: production batches will have 0.1-5% bad rows.
    # A try/except that aborts the run loses the other 99.5%. We catch the
    # error, capture enough context to debug, and keep going.
    for i, record in enumerate(records):
        try:
            valid.append(WeatherReading(**record))
        except ValidationError as e:
            errors.append({
                "index": i,
                "record": record,
                # WHY e.errors() not str(e): e.errors() returns a structured
                # list with field locations and error types, much easier to
                # log, group, and alert on than a free-form string.
                "errors": e.errors(),
            })
    return valid, errors


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
