"""Workshop 1 Part A solution: fail loudly at startup, not mid-run."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env from the workshop root regardless of where the script is run from.
_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")


def _required(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def _resolve(path_str: str) -> str:
    """Resolve relative paths against the workshop root."""
    p = Path(path_str)
    return str(p if p.is_absolute() else _ROOT / p)


INPUT_PATH = _resolve(_required("INPUT_PATH"))
OUTPUT_PATH = _resolve(_required("OUTPUT_PATH"))
VAT_RATE = float(os.environ.get("VAT_RATE", "0.21"))
