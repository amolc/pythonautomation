# Introduction to web scraping

**Course:** Automation using Python — Part 1  
**Module 7:** File Handling and Manipulation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Define web scraping in simple terms
- Understand when web scraping is appropriate
- Recognize the difference between downloading and parsing web content
- Identify common risks and ethical considerations

---

## Introduction

Web scraping means collecting information from web pages using software. Instead of copying text manually from a website, a Python script can download page content and extract the specific information you need.

This is useful when data is visible on a webpage but not easily available in a downloadable file or API.

---

## Key Concepts

### What web scraping involves

A basic scraping workflow usually has two steps:

1. Download the page content
2. Parse the HTML and extract useful data

### Web scraping vs APIs

If a website offers an API, that is often the better option because it is more structured and stable. Scraping is more fragile because websites can change their layout at any time.

### Common web scraping use cases

- collect product or pricing information
- capture headlines or announcements
- extract tables from public pages
- monitor website changes

### Risks and responsibilities

Before scraping a website, consider:

- whether the site allows automated access
- whether requests should be rate-limited
- whether the data is public and appropriate to collect
- whether an API already exists

Always scrape responsibly.

---

## Examples

### Example 1: A simple scraping workflow description

```python
steps = [
    "Send an HTTP request",
    "Receive HTML content",
    "Parse the HTML",
    "Extract target elements"
]

for step in steps:
    print(step)
```

### Example 2: Very basic HTML extraction idea

```python
html = "<h1>Daily Report</h1>"
print("Downloaded HTML:", html)
```

### Example 3: List possible scraping targets

```python
targets = ["titles", "links", "table rows", "prices"]
print(", ".join(targets))
```

---

## Notes

- Prefer APIs over scraping when possible.
- Web pages can change without warning, which can break a scraper.
- Add delays and avoid excessive requests.
- Review legal, ethical, and usage terms before scraping a site.

---

## Summary

- Web scraping is the process of downloading and extracting information from web pages.
- It is useful when data is available on a site but not through a better interface.
- Responsible scraping requires care, restraint, and awareness of site rules.

---

## Practice Exercises

1. Describe the two main steps in web scraping.
2. Explain one case where an API is better than scraping.
3. List three types of data that could be extracted from a webpage.

---

## Further Reading

- [Requests documentation](https://requests.readthedocs.io/)
- [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
