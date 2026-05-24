# Converting PDF files to other formats (e.g., text, images)

**Course:** Automation using Python — Part 1  
**Module 14:** PDF Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Explain why PDF conversion is useful in automation
- Convert PDF content into text or images conceptually and programmatically
- Recognize tools commonly used for PDF conversion workflows
- Understand when conversion is needed before further analysis

---

## Introduction

Sometimes a PDF is not the final format you need. An automation process may need plain text for parsing, images for visual review, or page images for OCR. Converting PDFs into other formats makes those next steps easier.

---

## Key Concepts

### Why convert PDFs

Conversion can help when you need to:

- parse text more easily
- archive page images
- prepare documents for OCR
- feed pages into image-processing workflows

### Common conversion targets

- PDF to text
- PDF to images
- PDF to extracted page-level content

### Tooling ideas

Depending on the task, conversion may involve:

- text extraction libraries
- PDF rendering tools
- OCR pipelines for scanned pages

### Conversion limits

Conversion quality depends on:

- document structure
- image quality
- fonts and layout
- whether the PDF is text-based or scanned

---

## Examples

### Example 1: Save extracted PDF text to a file

```python
from PyPDF2 import PdfReader

reader = PdfReader("report.pdf")
text = "\n".join(page.extract_text() or "" for page in reader.pages)

with open("report.txt", "w", encoding="utf-8") as file:
    file.write(text)
```

### Example 2: Conceptual page image conversion workflow

```python
steps = [
    "Open PDF",
    "Render each page as an image",
    "Save images for OCR or review"
]

for step in steps:
    print(step)
```

### Example 3: Decide next step after conversion

```python
pdf_type = "scanned"
if pdf_type == "scanned":
    print("Convert pages to images and run OCR")
else:
    print("Extract text directly")
```

---

## Notes

- Text extraction is often simpler than full visual conversion when the PDF already contains text.
- Scanned PDFs often require conversion plus OCR.
- Test conversion output quality before building downstream automation.
- Save converted outputs in organized folders.

---

## Summary

- Converting PDFs to text or images supports many automation workflows.
- The right conversion path depends on whether the PDF is text-based or scanned.
- Conversion quality should be validated before further processing.

---

## Practice Exercises

1. Extract text from a PDF and save it to a `.txt` file.
2. Describe a workflow for converting scanned PDF pages to images for OCR.
3. Explain one reason image conversion may be useful even when the final input is a PDF.

---

## Further Reading

- [PyPDF2 documentation](https://pypdf2.readthedocs.io/)
- [pytesseract project](https://github.com/madmaze/pytesseract)
