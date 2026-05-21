# Concatenation and Repetition

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Join strings and sequences
- Repeat sequence content
- Build simple report layouts

---

## Concatenation

```python
title = "Policy" + " " + "Renewal Report"
print(title)
```

## Repetition

```python
print("-" * 40)
print("DAILY CLAIMS SUMMARY")
print("-" * 40)
```

## List Concatenation

```python
batch_a = ["CLM001", "CLM002"]
batch_b = ["CLM003"]
all_claims = batch_a + batch_b
print(all_claims)
```

---

## Summary

- Use `+` for concatenation.
- Use `*` for repetition.
- Use carefully to keep output readable.

---

## Practice Exercises

1. Build `"May 2026 Premium Report"` using concatenation.
2. Print a 50-character separator.
3. Merge two policy lists.
