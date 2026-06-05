# Module 18: Building Web Apps with Flask

**Automation using Python — Part 1**

In this module, you will learn the fundamentals of building web applications and REST APIs using Flask. We will cover the concepts of HTTP routing, handling user requests, rendering dynamic HTML templates, serving static assets, and implementing robust RESTful web services. You will also learn how to connect your APIs to a SQLite database, perform automated data import using Pandas, and test your routes using Postman.

---

## Learning Outcomes

By the end of this module, you will be able to:
- Set up a virtual environment and install Flask.
- Write a minimal Flask application and run its development server.
- Extract parameters, headers, query strings, and JSON body data from user requests.
- Render dynamic web templates using the Jinja2 engine and serve static stylesheets.
- Define the principles of REST and explain the roles of HTTP methods (GET, POST, PUT, DELETE).
- Ingest data from CSV files using Pandas and store it inside a SQLite database.
- Build full CRUD (Create, Read, Update, Delete) endpoints that interact with SQLite.
- Export, configure, and import a Postman collection to test and validate your API.

---

## Prerequisites

- Python 3.9 or newer installed.
- Required packages: `flask`, `pandas`, and `sqlalchemy`.
- Set up and install these dependencies in your virtual environment:
  ```bash
  pip install flask pandas sqlalchemy
  ```

---

## Chapters

| # | Chapter | Topics |
|---|---------|--------|
| 1 | [Introduction to Flask and Setup](./introduction-to-flask-and-setup.md) | What Flask is, virtual environment setup, minimal application structure, running development server |
| 2 | [Routing and Request Handling](./routing-and-request-handling.md) | URL routing rules, dynamic URL path variables, parsing query strings, form fields, and JSON requests |
| 3 | [Rendering Templates and Static Files](./rendering-templates-and-static-files.md) | Jinja2 templates, rendering HTML, passing context variables, loops and conditionals in templates, static assets |
| 4 | [Introduction to REST APIs and HTTP Methods](./introduction-to-rest-apis-and-http-methods.md) | Concept of REST, URI design, HTTP verbs (GET, POST, PUT, DELETE), and HTTP response status codes |
| 5 | [Integrating CSV Data with Pandas and SQLite](./integrating-csv-data-with-pandas-and-sqlite.md) | Connecting to SQLite in Python, reading local CSV data into Pandas DataFrames, and storing them using SQL |
| 6 | [Building and Running REST APIs](./building-and-running-rest-apis.md) | Creating API endpoints, returning JSON using `jsonify`, implementing SQLite-backed GET, POST, PUT, and DELETE actions |
| 7 | [Testing APIs with Postman](./testing-apis-with-postman.md) | Setting up Postman, importing Collections, configuring environment URLs, and testing HTTP CRUD sequences |

---

## Module Capstone Exercise

Build a standalone Flask-based book inventory API named `book_manager.py` that implements the following requirements:

1. **Database Initialization**: On startup, read a local CSV file `initial_books.csv` (containing fields: `Title`, `Author`, `Genre`, `Price`) into a Pandas DataFrame, and save it to a SQLite database `books.db` inside a table called `books`.
2. **Web Routes**:
   - `GET /`: Renders an HTML template listing all books currently in the database.
3. **API Routes**:
   - `GET /api/books`: Returns a JSON list of all books. Allow filtering by `genre` via query parameters (e.g. `?genre=Fiction`).
   - `GET /api/books/<int:book_id>`: Returns details of a specific book by ID. Returns 404 if the book does not exist.
   - `POST /api/books`: Adds a new book. Requires JSON containing `Title`, `Author`, `Genre`, and `Price`. Returns the created book details and a `201 Created` status code.
   - `PUT /api/books/<int:book_id>`: Updates an existing book's details. Returns a `200 OK` status with the updated record, or `404 Not Found` if missing.
   - `DELETE /api/books/<int:book_id>`: Deletes a book by its ID. Returns a success status code.
4. **Validation**: Ensure that your API responses return the correct content types and status codes. Test all endpoints using the provided Postman collection.
