# Automating image manipulation tasks (e.g., resizing, cropping, filtering)

**Course:** Automation using Python — Part 1  
**Module 15:** Image Processing with Python

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Automate common image transformations with Python
- Resize, crop, and apply simple filters to images
- Process multiple images using repeatable rules
- Prepare image files for later automation steps

---

## Introduction

Image files often need preprocessing before they can be shared, analyzed, or passed into later automation steps. For example, images may need to be resized for a website, cropped to remove unwanted borders, or filtered to improve readability. Python can automate these tasks efficiently.

---

## Key Concepts

### Common image-processing tasks

Typical automation tasks include:

- resizing images
- cropping images
- rotating images
- converting formats
- applying filters or enhancements

### Why preprocessing matters

Preprocessing helps make later steps more consistent, especially if the images will be used for OCR, recognition, or reporting.

### Useful libraries

A common choice is the `Pillow` library (`PIL`), which supports many basic image operations.

### Batch processing pattern

A simple pattern is:

1. load input images
2. apply one or more transformations
3. save processed outputs

---

## Examples

### Example 1: Resize an image

```python
from PIL import Image

image = Image.open("photo.jpg")
resized = image.resize((300, 200))
resized.save("photo_resized.jpg")
```

### Example 2: Crop an image

```python
from PIL import Image

image = Image.open("photo.jpg")
cropped = image.crop((50, 50, 250, 200))
cropped.save("photo_cropped.jpg")
```

### Example 3: Process multiple images in a folder

```python
from pathlib import Path
from PIL import Image

for image_path in Path("input_images").glob("*.jpg"):
    image = Image.open(image_path)
    resized = image.resize((200, 200))
    output_path = Path("output_images") / image_path.name
    resized.save(output_path)
```

---

## Notes

- Install Pillow with `pip install pillow` before running examples.
- Keep original image files unchanged during testing.
- Use consistent output dimensions when processing batches.
- Validate visual quality after transformations.

---

## Summary

- Python can automate many repetitive image-processing tasks.
- Resizing, cropping, and batch transformation are common workflow steps.
- Preprocessed images are often easier to analyze or share later.

---

## Practice Exercises

1. Resize one image and save the result with a new file name.
2. Crop an image to a selected rectangle.
3. Process all `.jpg` files in a folder and save resized copies.

---

## Further Reading

- [Pillow documentation](https://pillow.readthedocs.io/)
