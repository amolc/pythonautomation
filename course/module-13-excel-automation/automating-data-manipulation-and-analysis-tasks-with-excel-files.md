# Automating data manipulation and analysis tasks with Excel files

**Course:** Automation using Python — Part 1  
**Module 13:** Excel Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Clean and transform Excel data with Python
- Perform simple summaries and aggregations
- Automate repeated spreadsheet analysis tasks
- Create reusable workflows for Excel-based reporting

---

## Introduction

Reading an Excel file is only the beginning. In real automation work, scripts often need to clean the data, calculate metrics, filter records, and export a useful summary. Python is especially strong at turning raw spreadsheet data into structured outputs.

---

## Key Concepts

### Common transformations

Automation tasks often include:

- removing empty rows
- renaming columns
- converting data types
- filtering records
- grouping and summarizing values

### Analysis with `pandas`

DataFrames make it easy to automate business analysis such as totals, counts, averages, and grouped summaries.

### Reusable reporting workflows

A useful pattern is:

1. load workbook data
2. clean and validate it
3. apply business rules
4. export the result

### Why consistency matters

Automated spreadsheet analysis is most reliable when input files follow a stable structure.

---

## Examples

### Example 1: Filter rows

```python
import pandas as pd

df = pd.DataFrame({
    "branch": ["North", "South", "North"],
    "premium": [1200, 900, 1500]
})

north_df = df[df["branch"] == "North"]
print(north_df)
```

### Example 2: Group and summarize

```python
import pandas as pd

df = pd.DataFrame({
    "branch": ["North", "South", "North"],
    "premium": [1200, 900, 1500]
})

summary = df.groupby("branch")["premium"].sum()
print(summary)
```

### Example 3: Clean missing values

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", None, "Ravi"],
    "status": ["active", "inactive", None]
})

clean_df = df.fillna("unknown")
print(clean_df)
```

---

## Notes

- Keep cleaning and transformation steps explicit.
- Validate important columns before running analysis.
- Save outputs with clear file names or dates.
- Test the workflow on representative sample workbooks.

---

## Summary

- Python can automate spreadsheet cleaning, transformation, and summary generation.
- `pandas` is especially effective for repeated Excel analysis tasks.
- Reliable Excel automation depends on both code and stable input structure.

---

## Practice Exercises

1. Filter an Excel dataset to keep only rows matching one branch.
2. Group data by a category column and calculate a sum.
3. Replace missing values in a DataFrame with a default label.

---

## Further Reading

- [pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)
