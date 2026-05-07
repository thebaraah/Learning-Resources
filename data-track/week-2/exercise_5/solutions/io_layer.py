"""Reference solution: I/O layer for Exercise 5.

WHY io_layer.py and not io.py: 'io' is a stdlib module. Naming our
file io.py would shadow it (Gotcha #5 from the gotchas chapter).
"""
import json
from dataclasses import asdict


def read_users(path: str) -> list[dict]:
    """Read JSON, return raw list of dicts. No filtering, no validation."""
    # WHY encoding="utf-8": Windows defaults to cp1252 for text files.
    # Pinning UTF-8 makes the read identical on macOS / Linux / Windows
    # and avoids decode errors when names carry non-ASCII characters.
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_users(users: list, path: str) -> None:
    """Save users (User instances or plain dicts) as JSON."""
    # WHY normalise via asdict if dataclass else passthrough: the
    # orchestrator may hand us either dataclass instances or plain
    # dicts depending on whether validation was applied. asdict()
    # only works on dataclasses; for plain dicts we serialise as-is.
    payload = [asdict(u) if hasattr(u, "__dataclass_fields__") else u for u in users]
    # WHY encoding="utf-8" + ensure_ascii=False: same locale-portability
    # reason as the read above. ensure_ascii=False writes real Unicode
    # characters (e.g. "Renée") instead of escape sequences ("Ren\u00e9e"),
    # so the JSON file is human-readable and round-trips byte-identical.
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
