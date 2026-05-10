"""Gotcha #2 demo: the mutable-default trap.

A regular function silently shares the default list across calls.
A dataclass refuses to compile a mutable default and tells you.

Run: python mutable_default_trap.py
"""

from __future__ import annotations

from dataclasses import dataclass, field


def add_tag_bad(tag: str, tags: list = []) -> list:
    """Mutable default. Every call shares the SAME list."""
    tags.append(tag)
    return tags


def add_tag_good(tag: str, tags: list | None = None) -> list:
    """The fix: None sentinel + new list inside the function."""
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


# A dataclass with a mutable default raises ValueError immediately.
# Uncomment to see the crash:
# @dataclass
# class TaggedItemBad:
#     tags: list = []  # ValueError: mutable default <class 'list'> is not allowed


# The dataclass fix: field(default_factory=...).
@dataclass
class TaggedItemGood:
    tags: list = field(default_factory=list)


if __name__ == "__main__":
    print("BAD function:")
    print(f"  add_tag_bad('a') = {add_tag_bad('a')}")
    print(f"  add_tag_bad('b') = {add_tag_bad('b')}  <-- 'a' leaked!")

    print("\nGOOD function:")
    print(f"  add_tag_good('a') = {add_tag_good('a')}")
    print(f"  add_tag_good('b') = {add_tag_good('b')}  <-- isolated")

    print("\nGOOD dataclass:")
    a = TaggedItemGood()
    b = TaggedItemGood()
    a.tags.append("x")
    print(f"  a.tags = {a.tags}, b.tags = {b.tags}  <-- separate lists")
