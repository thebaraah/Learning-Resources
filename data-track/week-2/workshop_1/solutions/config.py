"""Workshop 1 Part A solution: fail loudly at startup, not mid-run."""

import os

from dotenv import load_dotenv

load_dotenv()


def _required(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


INPUT_PATH = _required("INPUT_PATH")
OUTPUT_PATH = _required("OUTPUT_PATH")
VAT_RATE = float(os.environ.get("VAT_RATE", "0.21"))
