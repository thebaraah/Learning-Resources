import pandas as pd


def section_1_string_operations():
    print("--- Section: Vectorized String Operations ---")
    users = pd.DataFrame(
        {
            "name": ["Alice Smith", "Bob Jones", "Chloe van Dam"],
            "email": ["  Alice@Gmail.COM", "bob@example.com ", "chloe@gmail.com"],
            "country": ["nl", "be", "de"],
        }
    )
    users["email"] = users["email"].str.strip().str.lower()
    users["country"] = users["country"].str.upper()
    users["has_gmail"] = users["email"].str.contains("@gmail.com", na=False)
    users["first_name"] = users["name"].str.split(" ").str[0]
    print(users)


def section_2_pattern_matching():
    print("\n--- Section: Pattern Matching and Extraction ---")
    phones = pd.DataFrame(
        {
            "phone": ["06 12345678", "06 23456789", "020 7654321"],
        }
    )
    phones["phone_clean"] = phones["phone"].str.replace(" ", "", regex=False)
    # Extract the first 2-3 digit area code
    phones["area_code"] = phones["phone_clean"].str.extract(r"(\d{2,3})")
    print(phones)


def section_3_parsing_dates():
    print("\n--- Section: Parsing Dates ---")
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4],
            "order_date": ["2024-01-05", "2024-02-14", "2024-03-22", "invalid"],
        }
    )
    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="coerce",
        format="%Y-%m-%d",
    )
    print("Parsed dates (invalid becomes NaT):")
    print(orders)
    print("\nMissing dates:", orders["order_date"].isna().sum())


def section_4_date_components():
    print("\n--- Section: Date Components and Arithmetic ---")
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "order_date": pd.to_datetime(["2024-01-05", "2024-02-14", "2024-03-22"]),
            "amount": [120, 90, 200],
        }
    )
    orders["year"] = orders["order_date"].dt.year
    orders["month"] = orders["order_date"].dt.month
    orders["weekday"] = orders["order_date"].dt.day_name()
    # Use a fixed reference date so output is deterministic
    reference = pd.Timestamp("2024-04-01")
    orders["days_ago"] = (reference - orders["order_date"]).dt.days
    print(orders)


def section_5_timezones_resampling():
    print("\n--- Section: Time Zones and Resampling ---")
    orders = pd.DataFrame(
        {
            "order_date": pd.to_datetime(["2024-01-05", "2024-01-20", "2024-02-14", "2024-02-28"]),
            "amount": [120, 80, 90, 200],
        }
    )
    orders["order_date"] = orders["order_date"].dt.tz_localize("UTC")
    orders["order_date_eu"] = orders["order_date"].dt.tz_convert("Europe/Amsterdam")

    monthly = orders.set_index("order_date_eu").resample("ME")["amount"].sum()
    print("Monthly totals (resampled):")
    print(monthly)


if __name__ == "__main__":
    section_1_string_operations()
    section_2_pattern_matching()
    section_3_parsing_dates()
    section_4_date_components()
    section_5_timezones_resampling()
