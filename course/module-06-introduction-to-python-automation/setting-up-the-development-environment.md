# Setting up the development environment

**Course:** Automation using Python — Part 1  
**Module 6:** Introduction to Python Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Install Python and verify the installation
- Create and activate a virtual environment
- Install project dependencies with `pip`
- Organize a basic folder structure for automation scripts
- Use a code editor and terminal effectively for Python work

---

## Introduction

Before building automation scripts, you need a reliable development environment. A good setup makes it easier to install packages, run scripts, debug errors, and keep project dependencies organized.

A typical Python automation environment includes:

- Python installed on your machine
- A terminal or command prompt
- A code editor such as Zed, VS Code, or PyCharm
- A project folder
- A virtual environment
- A `requirements.txt` file for dependencies

---

## Key Concepts

### Step 1: Install Python

Download Python from the official website:

- [https://www.python.org/downloads/](https://www.python.org/downloads/)

After installation, verify it in the terminal:

```bash
python --version
```

Some systems use:

```bash
python3 --version
```

If Python is installed correctly, you should see a version number such as `Python 3.12.0`.

### Step 2: Create a project folder

A simple project structure helps keep automation scripts organized.

Example:

```text
automation-project/
├── scripts/
├── data/
├── output/
├── logs/
└── requirements.txt
```

This structure separates source scripts, input files, generated outputs, and logs.

### Step 3: Create a virtual environment

A virtual environment isolates packages for one project so they do not conflict with other Python projects.

Create it with:

```bash
python -m venv venv
```

Or on some systems:

```bash
python3 -m venv venv
```

This creates a local folder named `venv`.

### Step 4: Activate the virtual environment

#### On macOS or Linux

```bash
source venv/bin/activate
```

#### On Windows (Command Prompt)

```bash
venv\Scripts\activate
```

Once activated, package installations with `pip` will go into the virtual environment instead of the global Python installation.

### Step 5: Install required libraries

For example:

```bash
pip install requests pandas openpyxl
```

Save the installed packages to a requirements file:

```bash
pip freeze > requirements.txt
```

This lets you recreate the environment later with:

```bash
pip install -r requirements.txt
```

### Step 6: Choose a code editor

A good editor improves productivity with:

- Syntax highlighting
- Auto-completion
- File explorer
- Integrated terminal
- Search across files

Popular choices include Zed, VS Code, and PyCharm. For this course, any editor that can run Python files and open folders is enough.

### Step 7: Run a test script

Create a file such as `scripts/hello_automation.py` and run:

```python
print("Automation environment is ready!")
```

Then execute it:

```bash
python scripts/hello_automation.py
```

If the message appears, your environment is working.

### Step 8: Basic setup best practices

- Use one virtual environment per project.
- Keep dependency lists in `requirements.txt`.
- Do not store secrets directly in scripts.
- Use clear folder names for data and outputs.
- Test installation and script execution before starting larger work.

---

## Examples

### Example 1: Create useful project folders in Python

```python
from pathlib import Path

for folder_name in ["scripts", "data", "output", "logs"]:
    Path(folder_name).mkdir(exist_ok=True)

print("Project folders created")
```

### Example 2: Simple dependency notes file

```python
libraries = ["requests", "pandas", "openpyxl"]

for library in libraries:
    print(f"Install with: pip install {library}")
```

### Example 3: Check current Python executable

```python
import sys

print("Python executable:", sys.executable)
```

This is useful when confirming that your script is running inside the expected virtual environment.

---

## Notes

- If `python` does not work, try `python3`.
- If `pip` fails, use `python -m pip install package_name`.
- If a library installs globally by mistake, check whether the virtual environment is activated.
- Avoid keeping large generated files in the same folder as source code.
- When working in teams, share `requirements.txt`, not your `venv` folder.

---

## Summary

- A good Python automation setup includes Python, a project folder, a virtual environment, and a code editor.
- Virtual environments keep project dependencies isolated and manageable.
- Verifying the setup early helps prevent package and execution issues later.

---

## Practice Exercises

1. Install Python and verify the version from your terminal.
2. Create a new folder for an automation project and add `scripts`, `data`, and `output` directories.
3. Create a virtual environment, install one package, and save the dependencies to `requirements.txt`.

---

## Further Reading

- [Python Packaging User Guide](https://packaging.python.org/)
- [venv documentation](https://docs.python.org/3/library/venv.html)
- [pip documentation](https://pip.pypa.io/en/stable/)
