"""Workshop 2 Part A: when do you need a class?

Four snippets to discuss. For each one: which tool fits, and why?

Decision framework:
  1. Pure input -> output, no state?          -> function
  2. Holds state across calls?                -> class with __init__ + self
  3. Utility that belongs ON a class
     but needs no instance or class state?    -> @staticmethod
  4. Alternative constructor or factory
     that needs access to the class itself?   -> @classmethod

Refactoring signal: when a function starts needing to "remember" things between
calls, or when you find yourself passing the same config object into five
different functions, that is when a class pays its way.
"""
from __future__ import annotations

from dataclasses import dataclass


# A: Pure function — no state, input -> output. A function is the right tool.
def apply_vat(price: float, rate: float = 0.21) -> float:
    return round(price * (1 + rate), 2)


# B: Regular class — holds connection state across calls. A class is the right tool.
class DatabaseConnector:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.connected = False

    def connect(self) -> None:
        self.connected = True


# C: @staticmethod — utility logic that belongs on the class conceptually but
# needs no access to the instance (self) or the class (cls).
# It is just a regular function namespaced under the class.
@dataclass
class Transaction:
    product_name: str
    price: float
    quantity: int
    revenue: float

    @staticmethod
    def is_valid_row(row: dict) -> bool:
        """Check a raw CSV row before constructing a Transaction."""
        return float(row.get("price", -1)) > 0 and int(row.get("quantity", 0)) > 0


# D: @classmethod — alternative constructor. Receives the class itself as 
# so it can call cls(...) without hardcoding the class name. Useful for
# building an instance from a different input format (e.g. a raw CSV row).
@dataclass
class TransactionV2:
    product_name: str
    price: float
    quantity: int
    revenue: float

    @classmethod
    def from_row(cls, row: dict, vat: float = 0.21) -> TransactionV2:
        price = float(row["price"])
        qty = int(row["quantity"])
        revenue = round(price * qty * (1 + vat), 2)
        return cls(
            product_name=row["product_name"].strip().title(),
            price=price,
            quantity=qty,
            revenue=revenue,
        )


# Discussion questions:
# 1. Could apply_vat be a @staticmethod on Transaction instead? Would that be better?
# 2. What would break if from_row used "TransactionV2(...)" instead of "cls(...)"?
# 3. At what point would you pull is_valid_row OUT of the class into a standalone function?
