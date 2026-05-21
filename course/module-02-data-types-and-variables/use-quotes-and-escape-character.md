# Use quotes and escape character

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Use single, double, and triple quotes properly
- Escape special characters safely
- Build clear messages for customer communication

---

## Quote Styles

```python
company = 'SafeLife Insurance'
message = "Policy renewal reminder"
email_body = """Dear Customer,
Your policy is due for renewal.
Regards,
Operations Team"""
```

---

## Escape Characters

| Escape | Use |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote inside string |

```python
note = "Customer said: \"Please share claim status today.\""
path = "C:\\insurance\\claims\\2026\\"
print(note)
print(path)
```

---

## Raw Strings

```python
pattern = r"^POL-\d{4}-\d{5}$"
```

Useful for regex and Windows paths.

---

## Summary

- Choose quote style for readability.
- Escape only what is required.
- Use raw strings when backslashes are frequent.

---

## Practice Exercises

1. Write a multi-line claim approval message using triple quotes.
2. Store `He said "policy is active"` correctly.
3. Define a Windows folder path string without errors.
