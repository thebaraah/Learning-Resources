"""Workshop 2 Part C solution: composable transforms."""

VAT_RATE = 0.21


def clean_names(rows: list[dict]) -> list[dict]:
    return [{**r, "product_name": r["product_name"].strip().title()} for r in rows]


def calculate_revenue(rows: list[dict]) -> list[dict]:
    out = []
    for r in rows:
        revenue = float(r["price"]) * int(r["quantity"])
        out.append({**r, "revenue": revenue, "vat": revenue * VAT_RATE})
    return out


def remove_invalid(rows: list[dict]) -> list[dict]:
    out = []
    for r in rows:
        try:
            if float(r["price"]) <= 0 or int(r["quantity"]) <= 0:
                continue
        except (ValueError, TypeError):
            continue
        out.append(r)
    return out
