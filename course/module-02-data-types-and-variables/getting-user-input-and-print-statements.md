# Getting User Input and Print statements

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Capture input with `input()`
- Convert user input to correct types
- Print clean operational output

---

## User Input

`input()` always returns a string.

```python
policy_id = input("Enter policy ID: ")
customer_age = int(input("Enter customer age: "))
base_premium = float(input("Enter base premium: "))
```

---

## Insurance Example

```python
policy_id = input("Policy ID: ").strip().upper()
base = float(input("Base premium: "))
rider = float(input("Rider premium: "))

print("Policy", policy_id, "total premium:", base + rider)
```

---

## Better Print Formatting

```python
print("Policy", "Status", sep=" | ")
print("POL-1001", "ACTIVE", sep=" | ")
print("Processing", end="...")
print("done")
```

---

## Summary

- Convert input explicitly (`int`, `float`).
- Use `.strip()` and case normalization for cleaner input.
- Use `print()` options like `sep` and `end` for readable logs.

---

## Practice Exercises

1. Ask for policy ID and premium, then print summary.
2. Ask claim amount and print GST-inclusive value.
3. Print a two-column status line with custom separator.
