# Module 3: Flow Control

**Automation using Python — Part 1**

This module teaches how Python makes decisions and repeats actions — core skills for automating underwriting checks, claim routing, and renewal reminders.

---

## Learning Outcomes

- Use operators for comparisons and logical checks
- Build decision paths with `if`, `elif`, and `else`
- Use loops to process multiple records efficiently
- Control loop behavior using `break`, `continue`, and loop conditions

---

## Chapters

1. [Python operators](./python-operators.md)
2. [If, else, elif clauses](./if-else-elif-clauses.md)
3. [Iteration](./iteration.md)
4. [Loops - for and while loops](./loops---for-and-while-loops.md)

---

## Module Capstone

Create `claims_triage.py` to:

1. Read a list of claim records
2. Categorize each claim as `LOW`, `MEDIUM`, or `HIGH` based on amount and fraud flags
3. Skip invalid records
4. Stop processing when a critical error record appears
5. Print category-wise count summary
