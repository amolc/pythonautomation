# Writing and Importing Modules

**Course:** Automation using Python — Part 1  
**Module 4:** Functions and Modules

---

## Learning Objectives

- Write your own module files
- Import modules and specific functions
- Use aliases for clearer code

---

## Create a Module

`premium.py`

```python
def total_premium(base, rider):
    return base + rider

def apply_tax(amount, rate=0.18):
    return amount + amount * rate
```

---

## Import and Use

`main.py`

```python
import premium

gross = premium.total_premium(18000, 2500)
final = premium.apply_tax(gross)
print(final)
```

Alternative import style:

```python
from premium import total_premium
print(total_premium(20000, 3000))
```

---

## Summary

- Put reusable logic into module files.
- Import using `import module` or `from module import name`.
- Prefer explicit imports for readability.

---

## Practice Exercises

1. Write a `claims.py` module with a `risk_level()` function.
2. Import and call it from `main.py`.
3. Add alias import and compare readability.
