# Extracting data from Excel worksheets and ranges

**Course:** Automation using Python — Part 1  
**Module 13:** Excel Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Read data from specific worksheets
- Extract selected ranges or subsets of spreadsheet data
- Target rows and columns relevant to an automation task
- Prepare worksheet data for further processing

---

## Introduction

Many Excel workbooks contain more data than an automation script actually needs. A script may need one sheet, a few columns, or a specific range of rows. Extracting only relevant data makes processing faster and more accurate.

---

## Key Concepts

### Worksheet selection

Excel workbooks may contain many sheets. Your script should know which one to read by sheet name or position.

### Column and row selection

When working with `pandas`, you can limit the imported data to selected columns or skip unnecessary rows.

### Range-like extraction

Excel libraries may let you work with precise cell ranges, while `pandas` is often best for structured tabular regions.

### Why focused extraction matters

Extracting only the needed area helps:

- reduce noise
- improve performance
- simplify downstream logic

---

## Examples

### Example 1: Read a specific worksheet

```python
import pandas as pd

df = pd.read_excel("report.xlsx", sheet_name="Claims")
print(df.head())
```

### Example 2: Read selected columns

```python
import pandas as pd

df = pd.read_excel("report.xlsx", sheet_name="Claims", usecols=["claim_id", "status"])
print(df)
```

### Example 3: Skip rows when importing

```python
import pandas as pd

df = pd.read_excel("report.xlsx", sheet_name="Claims", skiprows=2)
print(df.head())
```

---

## Notes

- Use clear sheet names instead of relying only on sheet position when possible.
- Restrict columns early to keep data handling simpler.
- Check header placement when worksheets include title rows or notes.
- Validate that the extracted range contains the expected data.

---

## Summary

- Worksheet and range extraction help target the right spreadsheet data.
- Focused imports reduce complexity and improve script reliability.
- `pandas` offers practical options for selecting sheets, columns, and rows.

---

## Practice Exercises

1. Read one named worksheet from an Excel file.
2. Import only two selected columns from a sheet.
3. Skip title rows at the top of a worksheet and load the table below them.

---

## Further Reading

- [pandas read_excel parameters](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
