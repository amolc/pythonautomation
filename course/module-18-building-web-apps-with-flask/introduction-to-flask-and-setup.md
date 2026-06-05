# Introduction to Flask and Setup

**Course:** Automation using Python — Part 1  
**Module 18:** Building Web Apps with Flask

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Explain what Flask is and why it is classified as a microframework.
- Create a virtual environment and install Flask using `pip`.
- Structure and write a minimal Flask application.
- Start the development server and run the application in debug mode.

---

## Introduction

In modern automation, running local scripts or CLI tools is often not enough. You may need to expose your Python functions so that other systems, team members, or frontend web pages can interact with them. 

**Flask** is a popular Python web framework that allows you to build web applications and API services with minimal boilerplate. It is known as a **microframework** because it does not require a specific database, form validation tool, or template engine by default. Instead, it provides the core routing and HTTP request-handling engine, letting you add external libraries (like Pandas or SQLite) as needed.

---

## Key Concepts

### What is a Web Framework?

A web framework is a collection of libraries and tools that handles standard web development tasks such as:
- Listening for network requests on specific ports.
- Mapping URLs (e.g., `/home`, `/api/users`) to Python functions.
- Formatting responses (HTML pages, file downloads, or JSON data).
- Parsing request details (cookies, form values, and files).

### Why Flask?

Flask is lightweight, highly extensible, and easy to learn. It is perfect for automation engineers who want to quickly build a dashboard, wrap their automation scripts in web APIs, or create lightweight microservices.

### Installation and Virtual Environments

To avoid cluttering your system's global Python installation, you should always run your web applications inside a **virtual environment**. A virtual environment isolates project-specific dependencies.

Commands to initialize and activate a virtual environment:
```bash
# Create the environment folder named 'venv'
python -m venv venv

# Activate on macOS/Linux:
source venv/bin/activate

# Activate on Windows (Command Prompt):
venv\Scripts\activate

# Activate on Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

Once activated, you install Flask using `pip`:
```bash
pip install Flask
```

---

## Examples

### Example 1: Instantiating a Minimal Flask App

Create a file named `app.py`. Write the following code:

```python
from flask import Flask

# Initialize the Flask application
# __name__ helps Flask locate templates and static files
app = Flask(__name__)

# Define a route for the homepage
@app.route("/")
def home():
    return "Hello from Flask! Your setup is successful."

if __name__ == "__main__":
    # Run the application locally
    app.run(debug=True)
```

### Example 2: Running the Development Server

There are two primary ways to run your Flask application:

1. **Directly running the Python script**:
   ```bash
   python app.py
   ```

2. **Using the Flask CLI command**:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development  # Deprecated in Flask 2.2+, use --debug instead
   flask run --debug
   ```
   *(On Windows Command Prompt, use `set` instead of `export`. On PowerShell, use `$env:`).*

Once run, you will see output indicating the server is running, typically at `http://127.0.0.1:5000/`. Open this URL in your browser to see your message.

---

## Notes

- **The `debug=True` Mode**: When debug mode is active, Flask enables a **hot reloader**, meaning the server will automatically restart whenever you save code changes. It also shows an **interactive debugger** in the browser if an unhandled exception occurs in your code.
- **Security Warning**: Never run your application with `debug=True` in a production environment, as it allows arbitrary code execution via the browser debugger.
- **Port Conflicts**: By default, Flask runs on port `5000`. If port 5000 is occupied (e.g. by AirPlay on macOS), you can change it in code: `app.run(port=8080, debug=True)` or in the CLI: `flask run --port=8080`.

---

## Summary

- Flask is a lightweight microframework used to build web applications and APIs.
- Virtual environments (`venv`) isolate your Flask dependencies from the rest of the OS.
- A Flask app uses decorators like `@app.route("/")` to bind a URL to a Python function.
- Debug mode provides automatic code reloading and error reporting during development.

---

## Practice Exercises

1. Create a Flask application that returns `"Welcome to the Python Automation Course!"` when visiting the homepage.
2. Add a second route `/health` that returns `"Server is healthy and running!"`.
3. Modify your Flask script to run on port `8000` with debug mode disabled. Confirm that the application loads on `http://127.0.0.1:8000/`.

---

## Further Reading

- [Flask Official Documentation - Installation](https://flask.palletsprojects.com/en/stable/installation/)
- [Flask Official Documentation - Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
