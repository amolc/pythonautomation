# Handling different Excel formats (e.g., .xls, .xlsx)

**Course:** Automation using Python — Part 1  
**Module 13:** Excel Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Distinguish between common Excel file formats
- Recognize compatibility issues between `.xls` and `.xlsx`
- Choose suitable tools for different workbook types
- Plan automation workflows that handle mixed Excel inputs

---

## Introduction

Excel files do not all use the same format. Older spreadsheets may use `.xls`, while newer workbooks commonly use `.xlsx`. Automation scripts need to recognize these differences because library support and features can vary by format.

---

## Key Concepts

### Common Excel formats

- `.xls` → older Excel binary format
- `.xlsx` → newer XML-based format
- `.csv` → plain text tabular data, not a full Excel workbook format

### Why format differences matter

Different formats may affect:

- which libraries can read the file
- support for formulas and styles
- speed and compatibility
- whether multiple sheets are available

### Tooling considerations

In modern workflows:

- `.xlsx` is commonly handled with `openpyxl`
- `.xls` may require older or specific reader support
- conversion may be useful when legacy files are involved

### Mixed-format automation

If a folder contains multiple Excel formats, scripts should detect file types before processing.

---

## Examples

### Example 1: Check file extensions

```python
from pathlib import Path

for file_path in Path("input").glob("*"):
    print(file_path.name, file_path.suffix)
```

### Example 2: Filter only `.xlsx` files

```python
from pathlib import Path

for file_path in Path("input").glob("*.xlsx"):
    print("Process:", file_path.name)
```

### Example 3: Decide processing path by extension

```python
file_name = "legacy_report.xls"

if file_name.endswith(".xlsx"):
    print("Use modern Excel reader")
elif file_name.endswith(".xls"):
    print("Use legacy-compatible reader")
else:
    print("Unsupported format")
```

---

## Notes

- Standardize on `.xlsx` when possible for simpler workflows.
- Check library support before promising compatibility with old files.
- Treat `.csv` differently from workbook formats.
- Validate input format early in the script.

---

## Summary

- Excel automation often involves more than one file format.
- `.xls` and `.xlsx` differ in structure and tooling support.
- Early format detection helps make automation more reliable.

---

## Practice Exercises

1. Write a script that prints file extensions for all files in a folder.
2. Filter a folder so only `.xlsx` files are selected.
3. Explain one reason old `.xls` files may require extra handling.

---

## Further Reading

- [pandas Excel I/O guide](https://pandas.pydata.org/docs/user_guide/io.html#excel-files)
