# Automating PDF generation and manipulation tasks

**Course:** Automation using Python — Part 1  
**Module 14:** PDF Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Generate simple PDF outputs from Python
- Perform basic PDF manipulation tasks such as merge or split
- Understand common document automation use cases
- Design repeatable PDF workflows for reports and documents

---

## Introduction

Automation does not only read PDFs; it can also generate and manipulate them. Common workflows include creating reports, merging documents, splitting large PDFs into smaller files, or assembling document packets for operations.

---

## Key Concepts

### Common PDF automation tasks

Examples include:

- generate a report PDF
- merge multiple PDFs
- split a multi-page PDF
- reorder pages
- add or extract selected pages

### Libraries and tools

Python libraries can help with PDF creation and manipulation, depending on the task.

Examples:

- `PyPDF2` for merge and split work
- document-generation libraries such as `reportlab` for creating PDFs

### Reliable document workflows

A good PDF automation process should define:

- input files
- output naming rules
- page or section logic
- validation checks

---

## Examples

### Example 1: Merge PDFs with `PyPDF2`

```python
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("part1.pdf")
merger.append("part2.pdf")
merger.write("merged.pdf")
merger.close()
```

### Example 2: Split pages from a PDF

```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("report.pdf")
writer = PdfWriter()
writer.add_page(reader.pages[0])

with open("first_page.pdf", "wb") as output_file:
    writer.write(output_file)
```

### Example 3: Describe document generation steps

```python
steps = ["Collect data", "Format content", "Create PDF", "Save output"]
for step in steps:
    print(step)
```

---

## Notes

- Use predictable output names for generated PDFs.
- Validate page counts and output files after manipulation.
- Test merge and split workflows on sample documents.
- Keep source files unchanged when possible.

---

## Summary

- Python can automate PDF generation and document manipulation tasks.
- Merge, split, and structured output workflows are common use cases.
- Clear inputs, outputs, and checks improve PDF automation reliability.

---

## Practice Exercises

1. Merge two PDF files into one output PDF.
2. Extract the first page of a PDF into a new file.
3. Describe one business process that could benefit from automated PDF generation.

---

## Further Reading

- [PyPDF2 user guide](https://pypdf2.readthedocs.io/)
- [ReportLab documentation](https://www.reportlab.com/documentation/)
