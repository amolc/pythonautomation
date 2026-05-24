# Reading and extracting data from PDF files using PyPDF2 or pdfplumber library

**Course:** Automation using Python — Part 1  
**Module 14:** PDF Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Read PDF files in Python
- Extract text from pages using common PDF libraries
- Recognize the difference between readable text PDFs and scanned PDFs
- Choose an appropriate extraction tool for simple automation tasks

---

## Introduction

PDF files are widely used for invoices, statements, reports, and official documents. Automation often requires reading these files to extract text, check values, or prepare data for later processing. Python libraries such as `PyPDF2` and `pdfplumber` help with many text-based PDF extraction tasks.

---

## Key Concepts

### PDFs are not always easy to parse

A PDF is designed for display, not always for structured extraction. Text order, spacing, and layout can vary.

### Text PDFs vs scanned PDFs

- **Text PDF**: contains selectable text that libraries can often extract
- **Scanned PDF**: contains images of pages and may require OCR instead of direct text extraction

### Common libraries

- `PyPDF2` for basic PDF reading and manipulation
- `pdfplumber` for more detailed text extraction and page analysis

### Extraction expectations

PDF extraction works best when:

- the PDF contains actual text
- page layout is relatively consistent
- the script targets clear labels or patterns

---

## Examples

### Example 1: Read text with `PyPDF2`

```python
from PyPDF2 import PdfReader

reader = PdfReader("report.pdf")
first_page = reader.pages[0]
text = first_page.extract_text()
print(text)
```

### Example 2: Extract text with `pdfplumber`

```python
import pdfplumber

with pdfplumber.open("report.pdf") as pdf:
    first_page = pdf.pages[0]
    text = first_page.extract_text()
    print(text)
```

### Example 3: Loop through pages

```python
from PyPDF2 import PdfReader

reader = PdfReader("report.pdf")
for page_number, page in enumerate(reader.pages, start=1):
    print(f"Page {page_number}")
    print(page.extract_text())
```

---

## Notes

- Install needed libraries before use, such as `pip install PyPDF2 pdfplumber`.
- Test extraction on real sample PDFs because layout quality varies.
- If the PDF is scanned, direct text extraction may fail and OCR may be required.
- Use pattern matching after extraction to locate specific fields.

---

## Summary

- Python can read and extract text from many PDF files.
- `PyPDF2` and `pdfplumber` are useful tools for text-based PDFs.
- PDF extraction quality depends heavily on the document structure.

---

## Practice Exercises

1. Open a PDF file and extract the first page’s text.
2. Loop through all pages of a PDF and print their text.
3. Explain why scanned PDFs may need OCR instead of direct extraction.

---

## Further Reading

- [PyPDF2 documentation](https://pypdf2.readthedocs.io/)
- [pdfplumber documentation](https://github.com/jsvine/pdfplumber)
