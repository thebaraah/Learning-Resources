# Week 1: Setup, Tools, CLI and Git

[📖 View on Notion](https://hub.hackyourfuture.nl/Practice-2af50f64ffc981479b34e4e4ad74fbc8?pvs=74)

# Exercise 3: The Precision Trap

**Concepts:** Floating Point Math, Debugging, Logic.

You are processing payments for a transaction system. You have a wallet with `0.1` bitcoin, and you receive `0.2` bitcoin. You want to check if you now have exactly `0.3` bitcoin to execute a trade.

**The Buggy Code:**
This code prints “Transaction failed?” even though 0.1 + 0.2 should equal 0.3.

```python
wallet = 0.1
wallet += 0.2

print(f"Wallet balance:{wallet}")

if wallet == 0.3:
    print("Transaction Success!")
else:
    print("Transaction failed?")
```

**Instructions:**

1. Run the code. Notice that the print statement says `Wallet balance: 0.3`, yet the `if` check fails. This is confusing!
1. Set a **breakpoint** on the `if wallet == 0.3:` line.
1. Start the debugger. Hover your mouse over the `wallet` variable (or look in the Variables pane).
1. What is the *actual* value of `wallet`?
1. Computers struggle with exact decimal math. Change the code to use the `round()` function to fix the comparison (e.g., round to 1 decimal place).