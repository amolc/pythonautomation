# Using BeautifulSoup and Requests libraries for web scraping

**Course:** Automation using Python — Part 1  
**Module 7:** File Handling and Manipulation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Use `requests` to download a web page
- Parse HTML with `BeautifulSoup`
- Extract simple elements such as titles, links, and text
- Understand basic scraper structure and error handling

---

## Introduction

Two popular Python libraries make beginner-friendly web scraping much easier:

- `requests` downloads page content
- `BeautifulSoup` parses HTML and helps extract information

Together, they support many simple automation tasks involving public web pages.

---

## Key Concepts

### Step 1: Send an HTTP request

The `requests` library is used to fetch a page:

```python
import requests

response = requests.get("https://example.com", timeout=10)
```

If the request succeeds, the page HTML will be in `response.text`.

### Step 2: Parse the HTML

Use `BeautifulSoup` to turn raw HTML into a searchable structure:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
```

### Step 3: Find elements

Common methods include:

- `find()`
- `find_all()`
- `get_text()`
- attribute access such as `tag["href"]`

### Handling failures

A scraper should handle common problems such as:

- network errors
- timeouts
- missing elements
- unexpected HTML changes

---

## Examples

### Example 1: Fetch a page title

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com", timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.get_text())
```

### Example 2: Extract all links

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com", timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a"):
    href = link.get("href")
    text = link.get_text(strip=True)
    print(text, href)
```

### Example 3: Extract headings safely

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com", timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

heading = soup.find("h1")
if heading:
    print(heading.get_text(strip=True))
else:
    print("No h1 heading found")
```

---

## Notes

- Install required libraries with `pip install requests beautifulsoup4`.
- Always use a timeout when making HTTP requests.
- Check whether elements exist before accessing them.
- Prefer simple, stable selectors over overly fragile parsing logic.

---

## Summary

- `requests` downloads web pages and `BeautifulSoup` parses them.
- Together they can extract structured information from HTML.
- Robust scrapers should handle missing data and request failures.

---

## Practice Exercises

1. Use `requests` to download `https://example.com` and print the status code.
2. Parse the page title with `BeautifulSoup`.
3. Print all links from a web page using `find_all("a")`.

---

## Further Reading

- [Requests documentation](https://requests.readthedocs.io/)
- [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
