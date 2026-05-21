#!/usr/bin/env python3
"""Generate 15 module folders and chapter markdown files."""

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
COURSE = BASE / "course"

# 15 folders: syllabus lists File Handling and Web Scraping both as "Module 7" — merged in folder 07.
MODULES: list[tuple[int, str, list[str]]] = [
    (
        1,
        "Python Basics",
        [
            "Introduction to Python",
            "Data Types",
            "Variables",
            "Data Structure",
            "Operations on Data Structure",
            "Inbuilt methods",
        ],
    ),
    (
        2,
        "Data Types and Variables",
        [
            "Data Types",
            "Understanding Variables",
            "Getting User Input and Print statements",
            "Use quotes and escape character",
            "Lists",
            "Tuples",
            "Dictionaries",
            "Sets",
            "Different Methods on data structures",
            "String Indexing and Slicing Strings",
            "Concatenation and Repetition",
            "Common String Methods",
            "String Formatting",
            "Namespaces",
            "Formatted String Literals (f-strings and .format() method)",
            "Built-in String Functions",
        ],
    ),
    (
        3,
        "Flow Control",
        [
            "Python Operators",
            "If, else, elif clauses",
            "Loops – for and while loops",
            "Iteration",
        ],
    ),
    (
        4,
        "Functions and Modules",
        [
            "Defining Functions",
            "Using Parameters and Return Values",
            "Using Arguments and Default Parameters",
            "Scope of Variables",
            "Modules and Packages",
            "Writing and Importing Modules",
        ],
    ),
    (
        5,
        "SQL",
        [
            "Introduction to SQL",
            "Types of Databases (Relational vs Non-Relational)",
            "Installing and Setting up Database (SQLite / PostgreSQL / MySQL)",
            "Basic Queries & Filtering Conditions",
            "Basic Queries with Aggregate Functions",
            "CRUD Operations",
            "SQL Joins",
            "Advanced Queries",
        ],
    ),
    (
        6,
        "Introduction to Python Automation",
        [
            "Overview of Automation and Its Benefits",
            "Introduction to Python Libraries for Automation",
            "Setting up the development environment",
        ],
    ),
    (
        7,
        "File Handling and Manipulation",
        [
            "Working with files and directories",
            "Automating file operations",
            "File searching and filtering",
            "Opening Files",
            "The os and os.path modules",
            "Reading files",
            "Writing into a file",
            "Appending data to a file",
            "Introduction to web scraping",
            "Using BeautifulSoup and Requests libraries for web scraping",
        ],
    ),
    (
        8,
        "GUI Automation",
        [
            "Introduction to GUI automation",
            "Automating mouse and keyboard actions",
            "Interacting with desktop applications",
        ],
    ),
    (
        9,
        "Database Automation",
        [
            "Introduction to database automation",
            "Connecting to databases using Python",
            "Automating database queries and data manipulation tasks",
        ],
    ),
    (
        10,
        "Task Scheduling and Automation",
        [
            "Introduction to task scheduling",
            "Using cron jobs and task scheduler libraries",
            "Automating recurring tasks and processes",
        ],
    ),
    (
        11,
        "Error Handling and Logging",
        [
            "Handling errors and exceptions in automation scripts",
            "Implementing logging for debugging and monitoring",
        ],
    ),
    (
        12,
        "Parallel Execution in Python",
        [
            "Threading",
            "Multiprocessing for parallel execution",
            "Implementing automation best practices",
            "Performance optimization techniques",
        ],
    ),
    (
        13,
        "Excel Automation",
        [
            "Introduction to Excel automation",
            "Reading and writing Excel files using pandas library",
            "Handling different Excel formats (e.g., .xls, .xlsx)",
            "Extracting data from Excel worksheets and ranges",
            "Automating data manipulation and analysis tasks with Excel files",
        ],
    ),
    (
        14,
        "PDF Automation",
        [
            "Reading and extracting data from PDF files using PyPDF2 or pdfplumber library",
            "Automating PDF generation and manipulation tasks",
            "Converting PDF files to other formats (e.g., text, images)",
        ],
    ),
    (
        15,
        "Image Processing with Python",
        [
            "Automating image manipulation tasks (e.g., resizing, cropping, filtering)",
            "Working with image recognition and OCR (Optical Character Recognition) for automation",
        ],
    ),
]


def slug(title: str) -> str:
    s = title.lower()
    for old, new in [
        ("–", "-"),
        ("—", "-"),
        ("&", "and"),
        ("/", "-"),
        ("(", ""),
        (")", ""),
        (".", ""),
        (",", ""),
        ("'", ""),
        ('"', ""),
        ("  ", " "),
    ]:
        s = s.replace(old, new)
    s = "".join(c if c.isalnum() or c in "- " else "-" for c in s)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-").replace(" ", "-")


def folder_name(num: int, title: str) -> str:
    return f"module-{num:02d}-{slug(title)}"


def chapter_content(module_num: int, module_title: str, chapter_title: str) -> str:
    return f"""# {chapter_title}

**Course:** Automation using Python — Part 1  
**Module {module_num}:** {module_title}

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Understand the core concepts covered in *{chapter_title}*
- Apply them in small Python examples
- Connect this topic to automation workflows where relevant

---

## Introduction

<!-- Add your teaching content here -->

This chapter covers **{chapter_title}** as part of Module {module_num}: {module_title}.

---

## Key Concepts

<!-- Expand each section with explanations, diagrams, and code samples -->

### Overview

_Add content._

### Examples

```python
# Example placeholder
```

### Notes

_Add important tips, pitfalls, and best practices._

---

## Summary

- _Key takeaway 1_
- _Key takeaway 2_
- _Key takeaway 3_

---

## Practice Exercises

1. _Exercise 1_
2. _Exercise 2_
3. _Exercise 3_

---

## Further Reading

- [Python documentation](https://docs.python.org/3/)
"""


def readme_content(module_num: int, module_title: str, chapters: list[str]) -> str:
    lines = [
        f"# Module {module_num}: {module_title}",
        "",
        "**Automation using Python — Part 1**",
        "",
        "## Chapters",
        "",
    ]
    for i, ch in enumerate(chapters, 1):
        lines.append(f"{i}. [{ch}](./{slug(ch)}.md)")
    lines.extend(["", "---", "", "_Add module overview and prerequisites here._", ""])
    return "\n".join(lines)


def main() -> None:
    COURSE.mkdir(parents=True, exist_ok=True)
    files = 0

    for num, title, chapters in MODULES:
        mod_dir = COURSE / folder_name(num, title)
        mod_dir.mkdir(parents=True, exist_ok=True)

        (mod_dir / "README.md").write_text(
            readme_content(num, title, chapters), encoding="utf-8"
        )
        files += 1

        for ch in chapters:
            (mod_dir / f"{slug(ch)}.md").write_text(
                chapter_content(num, title, ch), encoding="utf-8"
            )
            files += 1

    index = [
        "# Automation using Python — Part 1",
        "",
        "Structured course with **15 modules** (`module-01` … `module-15`). Each topic is a Markdown chapter.",
        "",
        "> **Module 07** includes both *File Handling* and *Web Scraping* chapters (syllabus lists these as two Module 7 blocks).",
        "",
        "## Modules",
        "",
    ]
    for num, title, _ in MODULES:
        index.append(f"{num}. [{title}](./{folder_name(num, title)}/README.md)")
    index.append("")

    (COURSE / "README.md").write_text("\n".join(index), encoding="utf-8")
    files += 1

    chapters_total = sum(len(c) for _, _, c in MODULES)
    print(
        f"Created {len(MODULES)} modules, {chapters_total} chapters, "
        f"{files} files under {COURSE}"
    )


if __name__ == "__main__":
    main()
