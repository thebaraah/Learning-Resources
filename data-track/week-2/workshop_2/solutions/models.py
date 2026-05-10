"""Workshop 2 Part B solution: validate at construction time."""

from dataclasses import dataclass


@dataclass
class Transaction:
    product_name: str
    price: float
    quantity: int
    revenue: float

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError(f"price cannot be negative: {self.price}")
        if not self.product_name.strip():
            raise ValueError("product_name cannot be empty")
