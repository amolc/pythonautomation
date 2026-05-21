# Lists

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Create and update lists
- Access list items with indexes/slices
- Use list methods in insurance automation

---

## Introduction

Lists are ideal for ordered and changing collections, such as claim IDs for a daily batch.

```python
claim_ids = ["CLM1001", "CLM1002", "CLM1003"]
print(claim_ids[0])
```

---

## Common Methods

```python
claim_ids.append("CLM1004")
claim_ids.insert(1, "CLM1099")
claim_ids.remove("CLM1002")
last_item = claim_ids.pop()

print(claim_ids)
print("Removed last:", last_item)
```

---

## Looping Through Lists

```python
premiums = [12000, 18500, 9900]
for premium in premiums:
    print("Premium:", premium)
```

---

## Summary

- Lists are mutable and ordered.
- Use methods like `append`, `remove`, and `pop`.
- Looping over lists is common in batch processing.

---

## Practice Exercises

1. Create a list of policy IDs and print the third item.
2. Add two new claim IDs and remove one.
3. Print only premiums greater than 10000.
