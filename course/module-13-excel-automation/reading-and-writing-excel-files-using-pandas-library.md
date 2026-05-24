# Reading and writing Excel files using pandas library

**Course:** Automation using Python — Part 1  
**Module 13:** Excel Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Read Excel files into pandas DataFrames
- Write DataFrames back to Excel files
- Select sheets and basic output options
- Use `pandas` for simple spreadsheet automation tasks

---

## Introduction

`pandas` is one of the most popular Python libraries for working with tabular data. It can read Excel sheets into DataFrames for analysis and transformation, then export the results back to Excel.

---

## Key Concepts

### Reading Excel files

Use `pd.read_excel()` to load spreadsheet data.

Common options include:

- file path
- sheet name
- selected columns
- header row

### Writing Excel files

Use `DataFrame.to_excel()` to create output files.

### Working with sheets

You can read a specific sheet by name or index. For multi-sheet output, `ExcelWriter` is often used.

### Why DataFrames help

Once Excel data is in a DataFrame, you can:

- filter rows
- rename columns
- group and summarize data
- clean missing values

---

## Examples

### Example 1: Read an Excel file

```python
import pandas as pd

df = pd.read_excel("reports.xlsx", sheet_name="Sheet1")
print(df.head())
```

### Example 2: Write a DataFrame to Excel

```python
import pandas as pd

data = {
    "branch": ["North", "South"],
    "premium": [1200, 900]
}

df = pd.DataFrame(data)
df.to_excel("summary.xlsx", index=False)
```

### Example 3: Write multiple sheets

```python
import pandas as pd

df1 = pd.DataFrame({"name": ["Asha", "Ravi"]})
df2 = pd.DataFrame({"status": ["active", "inactive"]})

with pd.ExcelWriter("output.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Customers", index=False)
    df2.to_excel(writer, sheet_name="Status", index=False)
```

---

## Notes

- Install required support libraries such as `openpyxl` when working with `.xlsx` files.
- Use `index=False` unless you explicitly want DataFrame index values in the sheet.
- Check sheet names carefully when reading from existing workbooks.
- Validate column names after import.

---

## Summary

- `pandas` makes Excel reading and writing straightforward.
- DataFrames provide a powerful structure for spreadsheet automation.
- Sheet selection and clean export settings improve reliability.

---

## Practice Exercises

1. Read an Excel sheet into a DataFrame and print the first five rows.
2. Create a DataFrame and save it to a new `.xlsx` file.
3. Write two DataFrames to separate sheets in one workbook.

---

## Further Reading

- [pandas read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
- [pandas to_excel](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)
