"""Pipeline CLI exercise.

A tiny CSV cleaner. Your job: wrap it with argparse so it accepts
--input, --output, and --log-level. Use the right log level for each
message in clean_rows().

Run (after you finish):
    python exercise_6.py --input data/messy_users.csv --output cleaned.json --log-level DEBUG
"""
import csv
import json
import logging


def clean_rows(rows):
    """Clean each row: lowercase email, skip rows missing a name."""
    cleaned = []
    skipped = 0

    for i, row in enumerate(rows):
        # FIXME 3a: this should be DEBUG (only useful when hunting a bug)
        logging.info(f"row {i}: starting")

        if not row.get("name", "").strip():
            # FIXME 3b: this should be WARNING (something the operator should know)
            logging.info(f"row {i}: missing name, skipping")
            skipped += 1
            continue

        row["name"] = row["name"].strip()
        row["email"] = row.get("email", "").strip().lower()
        cleaned.append(row)

    # This one IS info — a normal pipeline summary.
    logging.info(f"cleaned {len(cleaned)} rows, skipped {skipped}")
    return cleaned


def main():
    # TODO 1: parse arguments
    #   --input <path>      (required)
    #   --output <path>     (required)
    #   --log-level <name>  (optional, default "INFO", choices DEBUG/INFO/WARNING/ERROR)
    args = None  # replace with parser.parse_args()

    # TODO 2: configure the root logger to the chosen level
    # logging.basicConfig(level=getattr(logging, args.log_level))

    # TODO 4: read the CSV from args.input
    rows = []  # replace this — read with csv.DictReader

    cleaned = clean_rows(rows)

    # TODO 4 (continued): write the cleaned rows as JSON to args.output
    # with open(args.output, "w") as f:
    #     json.dump(cleaned, f, indent=2)


if __name__ == "__main__":
    main()
