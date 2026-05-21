# Introduction to Python

**Course:** Automation using Python — Part 1  
**Module 1:** Python Basics

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Explain what Python is and why it is widely used for automation
- Install Python and run code in the interactive shell and from a script file
- Write a simple program using `print()`, comments, and correct indentation
- Describe how Python source code is executed (interpreter, bytecode)
- Identify common tools used in automation workflows (terminal, editor, virtual environments)

---

## Introduction

**Python** is a high-level, general-purpose programming language created by Guido van Rossum and first released in 1991. Today it powers web applications, data science, DevOps tooling, and—most relevant to this course—**automation**: repeating tedious tasks such as renaming files, pulling data from APIs, filling spreadsheets, or scheduling scripts to run overnight.

Python reads like English more than many languages. That clarity, combined with a huge standard library and ecosystem (`requests`, `pandas`, `Selenium`, and more), makes it a practical first language for automators who are not full-time software engineers.

In this chapter you will run your first lines of Python and learn the habits—comments, indentation, running scripts—that every later module builds on.

---

## What Is Python?

| Characteristic | What it means for you |
|----------------|----------------------|
| **Interpreted** | Code runs line-by-line through the Python interpreter; no separate compile step before testing |
| **Dynamically typed** | You do not declare variable types upfront; types are determined at runtime |
| **Multi-paradigm** | Supports procedural, object-oriented, and functional styles |
| **Batteries included** | Rich **standard library** (files, dates, networking, JSON, etc.) without extra installs |
| **Cross-platform** | Same scripts run on Windows, macOS, and Linux with minimal changes |

### Why Python for automation?

- **Fast to write** — A 10-line script can replace an hour of manual clicks.
- **Readable** — Scripts you write today are understandable six months later.
- **Integrations** — Libraries talk to Excel, PDFs, browsers, databases, and cloud APIs.
- **Community** — Solutions to common automation problems are easy to find.

---

## Installing Python

1. Download the latest **Python 3** installer from [python.org/downloads](https://www.python.org/downloads/).
2. On Windows, check **“Add python.exe to PATH”** during installation.
3. Verify in a terminal (Command Prompt, PowerShell, or Terminal):

```bash
python3 --version
# Example output: Python 3.12.3
```

On some systems the command is `python` instead of `python3`.

### Virtual environments (recommended)

For real projects, create an isolated environment so package versions do not clash:

```bash
cd /path/to/your/project
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
# venv\Scripts\activate     # Windows
```

You will use virtual environments again in Module 6 when setting up automation tooling.

---

## Running Python Code

### 1. Interactive mode (REPL)

Type `python3` (or `python`) with no filename. You get a `>>>` prompt—**Read-Eval-Print Loop**:

```python
>>> 2 + 2
4
>>> print("Hello from the REPL")
Hello from the REPL
```

Press `Ctrl+D` (macOS/Linux) or `Ctrl+Z` then Enter (Windows) to exit.

Use the REPL for quick experiments. For repeatable automation, use **script files**.

### 2. Script files

Save code in a file ending with `.py`, then run:

```bash
python3 hello.py
```

Example `hello.py`:

```python
# My first automation-ready script
print("Automation using Python — Part 1")
print("Module 1: Python Basics")
```

Expected output:

```text
Automation using Python — Part 1
Module 1: Python Basics
```

---

## Your First Program

```python
# greet.py — demonstrates print and comments

# Single-line comment: ignored by Python, read by humans
print("Hello, World!")

# print() can show multiple values separated by spaces
name = "Alex"
print("Welcome,", name)
```

**Output:**

```text
Hello, World!
Welcome, Alex
```

### `print()` essentials

```python
print("Line 1")
print("Line 2", "Line 3")           # default separator is a space
print("A", "B", "C", sep="-")       # custom separator: A-B-C
print("Loading", end="...")         # custom end (default is newline)
print(" done")
```

Output:

```text
Line 1
Line 2 Line 3
A-B-C
Loading... done
```

---

## Comments and Documentation

| Style | Syntax | Use case |
|-------|--------|----------|
| Single-line | `# comment` | Explain *why* a line exists |
| Multi-line (informal) | Multiple `#` lines | Short notes |
| Docstring | `"""..."""` under a function | Official description (covered in Module 4) |

```python
# Bad: restates the obvious
x = x + 1  # add one to x

# Good: explains business logic
retry_count = retry_count + 1  # API allows max 3 retries per run
```

Comments are not executed. Over-commenting clutters code; under-commenting makes automation scripts hard to maintain.

---

## Indentation Matters

Python uses **indentation** (spaces, typically 4 per level) to define blocks—not curly braces `{}` like C or Java.

```python
status = "success"

if status == "success":
    print("Job finished OK")      # indented block belongs to if
    print("Sending notification")
else:
    print("Job failed")
```

**Wrong indentation causes `IndentationError`.** Never mix tabs and spaces in one file; use spaces only.

---

## How Python Executes Your Code

1. You run `python3 script.py`.
2. The interpreter **reads** the source file.
3. It **compiles** to bytecode (`.pyc` cached internally).
4. The **Python Virtual Machine** executes bytecode.
5. Output appears in the terminal (or logs, files, etc.).

For automation, the important idea is: **change the script → run again → same steps repeat reliably.**

---

## Tools You Will Use

| Tool | Role |
|------|------|
| **Terminal** | Run scripts, `pip install`, cron jobs |
| **Editor / IDE** | VS Code, PyCharm, Cursor—syntax highlighting, debugging |
| **Version control (Git)** | Track changes to automation scripts |
| **Package manager (`pip`)** | Install third-party libraries |

---

## Notes and Best Practices

- Always use **Python 3**; Python 2 is obsolete.
- Name script files with **lowercase** and **underscores**: `backup_files.py`, not `Backup Files.py`.
- Start scripts with a **shebang** only if you need direct execution on Unix: `#!/usr/bin/env python3`.
- Keep scripts in a project folder with a `venv` and a `requirements.txt` (later modules).
- Run small snippets in the REPL; commit working logic to `.py` files.

---

## Summary

- Python is an interpreted, readable language with strong support for automation and scripting.
- Install Python 3, verify with `python3 --version`, and prefer virtual environments for projects.
- Run code interactively (`>>>`) or via `python3 your_script.py`.
- Use `print()` for output, `#` for comments, and consistent **4-space indentation** for blocks.
- Automation success depends on repeatable scripts—not one-off REPL experiments.

---

## Practice Exercises

### Exercise 1 — Hello, Automator

Write a script `hello_automator.py` that prints exactly three lines:

1. Your name
2. The text: `I am learning Python automation`
3. Today's date as you would write it manually (e.g. `May 21, 2026`)

Run it from the terminal and confirm output.

---

### Exercise 2 — Formatted status report

Using only `print()` (no variables yet if you prefer), display a small “job report” like:

```text
=== Daily Backup Report ===
Status: STARTED
Files scanned: 0
Status: COMPLETE
```

Use `sep` or multiple `print()` calls so the header line is visually distinct.

---

### Exercise 3 — REPL exploration

In the interactive shell:

1. Evaluate `10 * 5 + 2`
2. Evaluate `"auto" + "mation"`
3. Use `print("Test", end="!")` twice in a row and observe how `end` changes line breaks

Write one sentence in a comment (in a `.py` file) describing what `end=` does.

---

### Exercise 4 — Fix the broken script

The script below has errors. Copy it into `broken.py`, fix it, and run successfully.

```python
if True
print("Indentation matters")
    print("This line should run only when True")
```

---

## Exercise Solutions (Check After You Try)

<details>
<summary>Click to reveal solutions</summary>

**Exercise 1** (example):

```python
print("Alex Morgan")
print("I am learning Python automation")
print("May 21, 2026")
```

**Exercise 2** (example):

```python
print("=== Daily Backup Report ===")
print("Status:", "STARTED", sep=" ")
print("Files scanned:", 0)
print("Status:", "COMPLETE", sep=" ")
```

**Exercise 3:** `"automation"` is printed; first `print` with `end="!"` does not add a newline, so the next output continues on the same line unless you reset with default `end="\n"`.

**Exercise 4:**

```python
if True:
    print("Indentation matters")
    print("This line should run only when True")
```

</details>

---

## Further Reading

- [Python documentation — Tutorial](https://docs.python.org/3/tutorial/)
- [Python documentation — Using Python on your platform](https://docs.python.org/3/using/index.html)
- PEP 8 — [Style Guide for Python Code](https://peps.python.org/pep-0008/) (naming and formatting conventions)
