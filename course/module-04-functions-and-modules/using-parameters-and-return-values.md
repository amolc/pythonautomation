# Using Parameters and Return Values

**Course:** Automation using Python — Part 1  
**Module 4:** Functions and Modules

---

## Learning Objectives

- Pass data into functions via parameters
- Return processed results
- Separate input, computation, and output

---

## Parameters vs Return Values

- **Parameters**: inputs to a function
- **Return value**: output from a function

```python
def apply_ncb_discount(premium, discount_percent):
    discount = premium * (discount_percent / 100)
    return premium - discount

final_premium = apply_ncb_discount(20000, 20)
print(final_premium)
```

---

## Multi-return Example

```python
def claim_summary(claim_amount):
    tax = claim_amount * 0.18
    total = claim_amount + tax
    return tax, total

tax, total = claim_summary(50000)
print(tax, total)
```

---

## Summary

- Parameters make functions flexible.
- Return values allow reuse of results in later logic.
- Avoid printing inside every function unless needed.

---

## Practice Exercises

1. Build a function that takes premium and rider and returns total.
2. Build a function returning `(approved_amount, rejected_amount)`.
3. Use returned values to print a final report line.
