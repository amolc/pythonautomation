# Working with image recognition and OCR (Optical Character Recognition) for automation

**Course:** Automation using Python — Part 1  
**Module 15:** Image Processing with Python

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Explain what OCR is and when it is useful
- Recognize how image recognition supports automation
- Use Python tools conceptually and practically for OCR workflows
- Identify image-quality factors that affect recognition accuracy

---

## Introduction

Some automation tasks require extracting text from images or scanned documents. OCR converts visible text in an image into machine-readable text. This is useful for invoices, forms, screenshots, scanned PDFs, and document images that cannot be read directly as plain text.

---

## Key Concepts

### What OCR does

OCR analyzes an image and attempts to detect and convert characters into text.

### Common automation uses

OCR is useful for:

- reading scanned forms
- extracting invoice numbers
- capturing text from screenshots
- processing scanned reports or receipts

### Image recognition vs OCR

- **OCR** focuses on reading text from images
- **Image recognition** may identify objects, shapes, logos, or template matches

### Why image quality matters

OCR accuracy depends heavily on:

- resolution
- contrast
- skew or rotation
- background noise
- font clarity

---

## Examples

### Example 1: OCR workflow idea

```python
steps = [
    "Load image",
    "Preprocess image",
    "Run OCR engine",
    "Clean extracted text"
]

for step in steps:
    print(step)
```

### Example 2: Use `pytesseract` conceptually

```python
from PIL import Image
import pytesseract

image = Image.open("invoice.png")
text = pytesseract.image_to_string(image)
print(text)
```

### Example 3: Improve OCR readiness conceptually

```python
quality_checks = ["high contrast", "clear text", "not blurry"]
print("OCR works best when images are:", quality_checks)
```

---

## Notes

- OCR usually works better after image preprocessing.
- Install both the Python package and the OCR engine when using tools such as Tesseract.
- Expect imperfect results and plan for validation where needed.
- Use OCR only when direct text sources are unavailable.

---

## Summary

- OCR converts text from images into machine-readable text.
- It is useful for scanned documents, screenshots, and image-based records.
- Good image quality and preprocessing strongly affect OCR accuracy.

---

## Practice Exercises

1. Describe the steps in a simple OCR workflow.
2. Explain two image-quality factors that affect OCR accuracy.
3. Name one business use case where OCR would help automate data extraction.

---

## Further Reading

- [pytesseract project](https://github.com/madmaze/pytesseract)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
