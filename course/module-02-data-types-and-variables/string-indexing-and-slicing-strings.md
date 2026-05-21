# String Indexing and Slicing Strings

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Access specific characters using index
- Extract segments with slicing
- Parse policy and claim references

---

## Indexing

```python
policy_id = "POL-2026-00981"
print(policy_id[0])   # P
print(policy_id[-1])  # 1
```

---

## Slicing

```python
print(policy_id[0:3])   # POL
print(policy_id[4:8])   # 2026
print(policy_id[-5:])   # 00981
```

---

## Insurance Example

```python
claim_ref = "CLM-MH-2026-7742"
state = claim_ref[4:6]
year = claim_ref[7:11]
print(state, year)
```

---

## Summary

- Indexing returns one character.
- Slicing returns part of a string.
- Useful for fixed-format IDs.

---

## Practice Exercises

1. Extract branch from `BR-DEL-0019`.
2. Print last 4 digits of policy number.
3. Reverse a claim string using slicing.
