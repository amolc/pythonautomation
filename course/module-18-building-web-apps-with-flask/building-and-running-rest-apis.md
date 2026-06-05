# Building and Running REST APIs

**Course:** Automation using Python — Part 1  
**Module 18:** Building Web Apps with Flask

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Establish and clean up SQLite database connections within a Flask application lifecycle.
- Implement REST API endpoints for all CRUD actions (Create, Read, Update, Delete) against database tables.
- Return structured JSON payloads using Flask's `jsonify` function.
- Enforce input validation and respond with appropriate HTTP status codes for success and failure states.

---

## Introduction

Exposing data and functionality via a REST API requires writing route handlers that execute SQL queries, capture client input, perform validation, and return structured JSON responses. 

In this chapter, we will build a complete, runnable product inventory REST API. The API will connect to a SQLite database and expose full CRUD endpoints.

---

## Key Concepts

### Database Lifecycles in Flask

When running a web server, opening and closing database connections for every query can be slow. However, keeping a single connection open indefinitely can lead to resource leaks and locking issues.

The best practice in Flask is to use a **helper function** to open a connection when a request arrives, and automatically close it when the request finishes. Flask provides the `g` object (a global namespace for temporary request-specific variables) and the `@app.teardown_appcontext` decorator to handle this cleanly.

### Returning JSON

In Flask 2.0 and newer, returning a Python dictionary or list from a route automatically serializes it to JSON and sets the response Content-Type header to `application/json`. However, using **`jsonify(data)`** is still highly recommended because it is more explicit and allows you to build complex structure combinations.

---

## Examples

### Example 1: Full CRUD API Implementation (`app.py`)

Here is a complete, single-file Flask API demonstrating all CRUD operations on a SQLite database named `inventory.db`:

```python
import sqlite3
from flask import Flask, jsonify, request, g

app = Flask(__name__)
DATABASE = "inventory.db"

# 1. Database Connection Helpers
def get_db():
    """Opens a connection to the database if not already open for this request."""
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Configure SQLite to return rows as dictionaries instead of tuples
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    """Automatically closes the database connection when the request finishes."""
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

# 2. Database Initialization
def init_db():
    """Helper to initialize the database table if it does not exist."""
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        """)
        db.commit()

# --- API ROUTES ---

# GET ALL / READ LIST
@app.route("/api/products", methods=["GET"])
def get_products():
    db = get_db()
    cursor = db.cursor()
    
    # Check if user filtered by category or name via query params (e.g. ?name=Pen)
    name_filter = request.args.get("name")
    
    if name_filter:
        cursor.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{name_filter}%",))
    else:
        cursor.execute("SELECT * FROM products")
        
    rows = cursor.fetchall()
    
    # Convert sqlite3.Row objects to standard Python dicts
    products = [dict(row) for row in rows]
    return jsonify(products)

# GET ONE / READ ITEM
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()
    
    if row is None:
        return jsonify({"error": "Product not found"}), 404
        
    return jsonify(dict(row))

# POST / CREATE
@app.route("/api/products", methods=["POST"])
def create_product():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data or "stock" not in data:
        return jsonify({"error": "Missing required fields (name, price, stock)"}), 400
        
    name = data["name"]
    price = data["price"]
    stock = data["stock"]
    
    # Simple input validation
    if price < 0 or stock < 0:
        return jsonify({"error": "Price and stock must be non-negative"}), 400
        
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
        (name, price, stock)
    )
    db.commit()
    
    # Retrieve the newly inserted product ID
    new_id = cursor.lastrowid
    
    return jsonify({"id": new_id, "name": name, "price": price, "stock": stock}), 201

# PUT / UPDATE
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    if not data or "name" not in data or "price" not in data or "stock" not in data:
        return jsonify({"error": "Missing required fields"}), 400
        
    db = get_db()
    cursor = db.cursor()
    
    # Verify product exists first
    cursor.execute("SELECT id FROM products WHERE id = ?", (product_id,))
    if cursor.fetchone() is None:
        return jsonify({"error": "Product not found"}), 404
        
    # Perform update query
    cursor.execute(
        "UPDATE products SET name = ?, price = ?, stock = ? WHERE id = ?",
        (data["name"], data["price"], data["stock"], product_id)
    )
    db.commit()
    
    return jsonify({"id": product_id, "name": data["name"], "price": data["price"], "stock": data["stock"]})

# DELETE
@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    db = get_db()
    cursor = db.cursor()
    
    # Verify product exists
    cursor.execute("SELECT id FROM products WHERE id = ?", (product_id,))
    if cursor.fetchone() is None:
        return jsonify({"error": "Product not found"}), 404
        
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    db.commit()
    
    return jsonify({"message": f"Product {product_id} deleted successfully"})

if __name__ == "__main__":
    # Ensure tables exist before starting the server
    init_db()
    app.run(debug=True)
```

---

## Notes

- **`row_factory = sqlite3.Row`**: By default, SQLite returns tuples (e.g. `("Laptop", 999.99)`). By setting `row_factory`, we can reference columns by name (e.g. `row["name"]`). Converting this with `dict(row)` yields a dictionary, which makes JSON serialization clean and dynamic.
- **Teardown App Context**: The `@app.teardown_appcontext` decorator ensures that the database connection is closed safely even if an error occurred during route processing.

---

## Summary

- Manage database connections inside Flask's request lifecycle using `g` and `@app.teardown_appcontext`.
- Return errors using standard HTTP status codes (like 400 for bad data and 404 for missing resources).
- Convert SQLite query row dictionaries into JSON arrays or objects using `jsonify()`.

---

## Practice Exercises

1. Write a script `sample_inserter.py` that connects to `inventory.db` and inserts three test items into the database so you have initial records to query.
2. Modify the `create_product()` POST route from Example 1 to make sure that the `name` column is unique. If a product with the same name already exists in the database, return a `409 Conflict` status code and a JSON error message `{"error": "Product name already exists"}`.
3. Write a new endpoint `GET /api/products/stats` that uses SQLite aggregation queries (`AVG`, `SUM`, `COUNT`) to return a JSON summary of your inventory:
   ```json
   {
     "total_products": 14,
     "average_price": 54.30,
     "total_value": 760.20
   }
   ```

---

## Further Reading

- [Flask Application Context](https://flask.palletsprojects.com/en/stable/appcontext/)
- [SQLite Row Objects Documentation](https://docs.python.org/3/library/sqlite3.html#row-objects)
