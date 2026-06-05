# Routing and Request Handling

**Course:** Automation using Python — Part 1  
**Module 18:** Building Web Apps with Flask

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Define URL routes containing dynamic path variables.
- Use Flask's variable converters to restrict parameter types.
- Access and parse query parameters from the URL.
- Parse form data and JSON payloads from incoming HTTP requests.

---

## Introduction

Web applications and APIs work by receiving requests and sending responses. To make your Flask app interactive, you need it to react differently depending on the URL path the user visits, and the parameters or data they submit. This is accomplished using **routing** and the global **`request`** object.

---

## Key Concepts

### Dynamic Routing and Converters

Routes are not limited to static strings. You can declare dynamic variables in your route path using angle brackets: `@app.route('/user/<username>')`.

By default, Flask treats path parameters as strings, but you can use **converters** to enforce specific types:
- `string`: Accepts any text without a slash (default).
- `int`: Accepts positive integers.
- `float`: Accepts positive floating-point values.
- `path`: Similar to string but accepts slashes (useful for file paths).

For example, `@app.route('/orders/<int:order_id>')` matches `/orders/123` but returns a 404 error for `/orders/abc`.

### The `request` Object

To inspect the details of an incoming connection, Flask provides the `request` object, which is imported from the `flask` library.

The `request` object contains:
1. **`request.args`**: A dictionary-like object (MultiDict) containing query parameters passed in the URL (e.g. `?name=Amol&role=admin`).
2. **`request.form`**: A dictionary containing form data sent via an HTML form POST request.
3. **`request.get_json()`**: A method that parses and returns the JSON payload sent in the request body (typically for APIs).
4. **`request.method`**: A string showing the HTTP method used (e.g. `"GET"`, `"POST"`).
5. **`request.headers`**: A dictionary containing HTTP headers.

---

## Examples

### Example 1: Dynamic Route Variables

This example shows how to use type-restricted dynamic variables:

```python
from flask import Flask

app = Flask(__name__)

# String dynamic path
@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

# Integer dynamic path
@app.route("/user/<int:user_id>")
def show_user(user_id):
    # user_id is automatically converted to an integer
    return f"Displaying profile for User ID: {user_id}"
```

### Example 2: Parsing Query Parameters

Query parameters are commonly used to filter or sort data (e.g. `http://127.0.0.1:5000/search?q=Python&page=2`).

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    # Use request.args.get() to safely handle missing keys
    query = request.args.get("q", default="all")
    page = request.args.get("page", default=1, type=int)
    
    return f"Searching for: '{query}' on page {page}"
```

### Example 3: Parsing JSON Request Payloads

For APIs, client systems often send data formatted as JSON.

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/api/users", methods=["POST"])
def create_user():
    # Retrieve JSON data from the body
    data = request.get_json()
    
    # Safely extract parameters
    name = data.get("name")
    email = data.get("email")
    
    if not name or not email:
        return "Missing name or email in request body", 400
        
    return f"Created user {name} with email {email} successfully!"
```

---

## Notes

- **Using `get()` vs brackets**: When retrieving parameters from `request.args` or `request.form`, always prefer `.get("key")` over `["key"]`. If the key does not exist, `.get()` returns `None` (or a default value you specify), whereas `["key"]` raises a `KeyError` (returning a 400 Bad Request error to the user).
- **Importing `request`**: The `request` object is a thread-safe local proxy. Do not define variables with the name `request` in your route functions to avoid shadowing the Flask object.

---

## Summary

- Route paths can contain variables, optionally filtered using type converters (like `<int:id>`).
- Flask parses incoming data and makes it accessible through properties on the `request` object.
- Use `request.args` for query parameters and `request.get_json()` for API JSON payloads.

---

## Practice Exercises

1. Create a route `/square/<int:number>` that calculates the mathematical square of the variable passed in the URL path and returns it.
2. Create a route `/report` that reads a query parameter named `format`. If `format=pdf`, return `"Generating PDF Report"`. If `format=csv`, return `"Generating CSV Report"`. For any other value (or if missing), return `"Generating HTML Report"`.
3. Create a POST route `/login` that reads form data variables `username` and `password`. If `username` is `"admin"` and `password` is `"secret"`, return `"Access Granted"`. Otherwise, return `"Access Denied"`.

---

## Further Reading

- [Flask Route Rules](https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules)
- [The Flask Request Object](https://flask.palletsprojects.com/en/stable/api/#incoming-request-data)
