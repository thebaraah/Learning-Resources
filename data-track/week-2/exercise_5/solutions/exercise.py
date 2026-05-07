"""Exercise 5: Refactor a "god function" (the capstone).

This is the final boss. The function `run()` below ties together every
mistake Week 2 has been pushing you to avoid: hardcoded paths, mixed
I/O and logic, no dataclass, mutation, no tests.

Your job: rebuild it as a clean pipeline using everything from Week 2.
"""
import json


# BAD: everything in one place
def run():
    with open("users.json") as f:
        users = json.load(f)

    active = []
    for user in users:
        if user["status"] == "active" and user["age"] >= 18:
            user["email"] = user["email"].lower().strip()
            active.append(user)

    with open("active_users.json", "w") as f:
        json.dump(active, f, indent=2)

    print(f"Processed {len(active)} users")


# Your refactored solution should:
#
#   1. Define a User dataclass with fields name, email, age, status.
#   2. Move INPUT_PATH and OUTPUT_PATH to a .env file and a config.py
#      module (Exercise 1's pattern).
#   3. Split run() into:
#        - read_users(path) -> list[dict]                   (I/O)
#        - filter_active_adults(users) -> list[dict]        (pure)
#        - clean_email(user) -> dict                         (pure, returns NEW dict)
#        - save_users(users, path) -> None                  (I/O)
#   4. main.py orchestrates the four functions in order, converting the
#      cleaned dicts to User instances before saving (use asdict to
#      serialise back).
#   5. Write at least 3 pytest tests for the pure functions.
#
# When done, AI_NOTES.md (one paragraph each):
#   - one helpful suggestion you accepted from an LLM and what it caught
#   - one suggestion you rejected and why
#
# Expected output of `python main.py` against the provided users.json:
#
#   Processed 3 users
#
#   active_users.json should contain Alice (alice@example.com),
#   Dan (dan@example.com), and Eve (eve@example.com). Bob is filtered
#   out (age 17), Carol is filtered out (status inactive).
#
# (You can keep `exercise.py` here as a comparison reference. The real
# refactored work goes in new files: models.py, transforms.py, io.py,
# config.py, main.py, tests/test_transforms.py.)


if __name__ == "__main__":
    # Run the BAD version once so you can see what the output looks like
    # before you refactor.
    run()
