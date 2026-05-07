"""Reference solution (in-place over the starter).

The TODO comment from the starter is preserved below; the fix is the
single-line `round(wallet, 1) == 0.3` change with a `# WHY ...:` note
explaining what's going on under the hood.

Teaches: floating-point representation is not exact (Gotcha #2);
round() at the boundary fixes the comparison.

`0.1 + 0.2` in IEEE 754 binary float is `0.30000000000000004`, NOT
`0.3`. Comparing two floats with `==` is almost always wrong. For
money or any decimal-precision domain the production fix is the
`decimal` module or working in integer cents / satoshis; rounding is
the quick-fix that's enough for the Week 1 lesson.
"""

wallet = 0.1
wallet += 0.2

# Prints `Wallet balance:0.30000000000000004` — the bit-exact
# representation, not the human-friendly value.
print(f"Wallet balance:{wallet}")

# TODO: Fix this comparison using round()
# WHY round(x, 1) instead of `wallet == 0.3`: rounding to 1 decimal
# place collapses the float-precision noise so the comparison
# reflects the *intent* (3 tenths == 3 tenths) rather than the
# bit-exact representation. For a real wallet you'd use Decimal
# (see the alt-fix at the bottom) or integer satoshis; this is the
# quick-fix the Week 1 lesson points at.
if round(wallet, 1) == 0.3:
    print("Transaction Success!")
else:
    print("Transaction failed?")

# Production-grade alternative worth knowing about even if we don't
# use it here:
#
#   from decimal import Decimal
#   wallet = Decimal("0.1") + Decimal("0.2")  # exactly 0.3
#   if wallet == Decimal("0.3"):              # True
#       ...
#
# Decimal stores numbers in base-10 internally so 0.1 + 0.2 is
# exactly 0.3. The cost: slower than float and more verbose to
# write. The benefit: no rounding errors. Worth it for money.
