"""Workshop 2 Part A: when do you need a class?

Two snippets side by side. Which one *needs* to be a class? Why?

Rule: data + config -> classes; logic + transforms -> functions.
"""


# A: Function (no state).
def apply_vat(price: float, rate: float = 0.21) -> float:
    return round(price * (1 + rate), 2)


# B: Class (has state).
class DatabaseConnector:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.connected = False

    def connect(self) -> None:
        self.connected = True


# A is input -> output. No state. A function is the right tool.
# B holds connection state across method calls. A class is the right tool.
