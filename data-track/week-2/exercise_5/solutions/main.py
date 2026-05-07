"""Reference solution: orchestrator for Exercise 5.

The ONLY file that knows about both I/O and business rules. Everything
else is single-purpose.
"""
from config import INPUT_PATH, OUTPUT_PATH
from io_layer import read_users, save_users
from models import User
from transforms import clean_emails, filter_active_adults


def run() -> None:
    raw = read_users(INPUT_PATH)
    actives = filter_active_adults(raw)
    cleaned = clean_emails(actives)

    # WHY convert to User dataclass at this point: the I/O layer reads
    # plain dicts; the transforms work on plain dicts (easy to test);
    # but before we save, we materialise as User instances so any
    # downstream consumer of `cleaned` gets the schema guarantee.
    users = [User(**u) for u in cleaned]

    save_users(users, OUTPUT_PATH)
    print(f"Processed {len(users)} users")


if __name__ == "__main__":
    run()
