# Exercise 4: Joining Two Tables

**Concepts:** `merge`, join types.

## Setup

The setup block at the top of `exercise.py` creates both `orders` and `customers` for you.

## Task

1. Join `orders` with `customers` on `customer_id` using a **left join**. Keep all orders even if no matching customer is found.
2. Count how many orders belong to each `segment` (`retail` vs `b2b`).

## Success criteria

- `enriched` has 5 rows (same as `orders`) — the left join keeps all original rows.
- Alice (customer_id 100) appears in two rows because she placed two orders.
- Segment counts: `retail` = 3, `b2b` = 2.

## Stretch

- Change to an inner join (`how='inner'`) and add a customer that has no matching orders. What happens to the row counts?
- Add a customer_id that does NOT exist in the customers table to the orders CSV. What does the left join produce for their `name` and `segment`?
