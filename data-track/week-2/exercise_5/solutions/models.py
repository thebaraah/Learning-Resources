"""Reference solution: User dataclass for Exercise 5."""
from dataclasses import dataclass


# WHY a dataclass instead of a dict: the field list is the schema. A
# typo like user["nmae"] crashes at runtime; user.nmae is caught by
# the editor before you save the file.
@dataclass
class User:
    name: str
    email: str
    age: int
    status: str
