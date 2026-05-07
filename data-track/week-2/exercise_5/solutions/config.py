"""Reference solution: centralised config for Exercise 5.

WHY one central place: every other module (transforms, io_layer, main)
imports paths from here. .env -> os.environ -> config -> rest of code.
"""
import os

from dotenv import load_dotenv


load_dotenv()


def _required(name: str) -> str:
    value = os.environ.get(name)
    if value is None:
        raise ValueError(f"{name} is required: add it to .env (see .env.example)")
    return value


INPUT_PATH = _required("INPUT_PATH")
OUTPUT_PATH = _required("OUTPUT_PATH")
