"""Reference solution for Exercise 1.

Centralised config module: load .env once, expose values as named imports.
"""
import os

from dotenv import load_dotenv


# WHY load_dotenv() at module import: this runs once, at the moment any
# other file does `from config import ...`. After this line, every key
# in .env is available via os.environ.
load_dotenv()


def _required(name: str) -> str:
    """Read an env var, fail loudly if missing.

    WHY raise instead of returning None: a None API key silently propagates
    until the first HTTP call, where the failure message is opaque
    ("Authorization: None"). Failing at import time points the finger at
    the missing config, not at the symptom.
    """
    value = os.environ.get(name)
    if value is None:
        raise ValueError(f"{name} is required: add it to .env (see .env.example)")
    return value


API_KEY = _required("API_KEY")
BASE_URL = _required("BASE_URL")
