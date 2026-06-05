# Introduction to REST APIs and HTTP Methods

**Course:** Automation using Python — Part 1  
**Module 18:** Building Web Apps with Flask

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Define what a REST API is and identify its core constraints.
- Explain the role and behavior of the main HTTP methods (GET, POST, PUT, DELETE).
- Map HTTP methods directly to standard CRUD operations.
- Select and return appropriate HTTP status codes for various API outcomes.

---

## Introduction

In software automation, system integration is key. Scripts need to fetch data from database servers, trigger workflows on build machines, or submit stats to reporting dashboards. The industry-standard way for systems to talk to each other over the network is through **REST APIs** (Representational State Transfer Application Programming Interfaces).

Understanding how REST APIs work is essential for writing code that integrates with web services, cloud providers, and internal backend platforms.

---

## Key Concepts

### What is REST?

**REST** is an architectural style for designing networked applications. It relies on a stateless, client-server protocol—almost always HTTP.

Core concepts of REST:
- **Resources**: Any entity or object you want to expose (e.g. a `user`, a `product`, a `file`). Resources are identified by logical URIs (Uniform Resource Identifiers).
- **Statelessness**: Every request from a client must contain all the information needed to understand and complete the request. The server does not store session memory about the client.
- **Representations**: The client requests a resource, and the server returns a representation of that resource (almost always formatted as JSON in modern APIs).

### HTTP Methods (Verbs) and CRUD

REST uses standard HTTP methods to represent operations. They map directly to standard CRUD (Create, Read, Update, Delete) database operations:

| HTTP Method | CRUD Operation | Description | Safe? | Idempotent? |
|---|---|---|---|---|
| **GET** | Read | Retrieve a resource or a collection of resources. | Yes | Yes |
| **POST** | Create | Create a new resource with data from the request body. | No | No |
| **PUT** | Update | Replace or fully update an existing resource. | No | Yes |
| **DELETE** | Delete | Remove a specified resource. | No | Yes |

* **Safe**: An HTTP method is safe if it does not modify the server state (it only reads data).
* **Idempotent**: An HTTP method is idempotent if executing it multiple times yields the same state on the server as running it once.

### HTTP Response Status Codes

Servers must notify clients about the result of their requests using standard three-digit HTTP status codes:

- **2xx (Success)**
  - `200 OK`: Request succeeded.
  - `201 Created`: Request succeeded and a new resource was created (commonly used for POST).
- **4xx (Client Errors)**
  - `400 Bad Request`: The request had invalid syntax or missing required parameters.
  - `401 Unauthorized`: Authentication is required or has failed.
  - `403 Forbidden`: The client is authenticated but does not have permission for the resource.
  - `404 Not Found`: The requested resource could not be found on the server.
  - `405 Method Not Allowed`: The resource exists, but the request used an HTTP method that is not supported.
- **5xx (Server Errors)**
  - `500 Internal Server Error`: The server encountered an unexpected error and could not complete the request.

---

## Examples

### Example 1: RESTful Endpoint Design

A properly designed REST API organizes endpoints around nouns (plural) representing resources, using the HTTP verb to describe the action:

- `GET /api/books` - Retrieve all books (Read list)
- `GET /api/books/45` - Retrieve book with ID 45 (Read item)
- `POST /api/books` - Add a new book (Create)
- `PUT /api/books/45` - Update book 45 (Update)
- `DELETE /api/books/45` - Remove book 45 (Delete)

*Avoid endpoints like `/api/getBooks`, `/api/createBook`, or `/api/deleteBook/45` because they contain verbs in the URI, violating REST design standards.*

### Example 2: Implementing Route Methods in Flask

By default, Flask routes only respond to `GET` requests. To support other methods (like `POST` or `DELETE`), you must specify them in the `@app.route` decorator's `methods` list:

```python
from flask import Flask, request

app = Flask(__name__)

# This route supports both GET and POST requests
@app.route("/api/books", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        return "Returning list of books..."
    elif request.method == "POST":
        return "Book created successfully!", 201
```

### Example 3: Returning Specific HTTP Status Codes

You can return status codes from route functions by returning a tuple: `(response_body, status_code)`:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/api/verify", methods=["POST"])
def verify():
    data = request.get_json()
    if not data or "token" not in data:
        # Return 400 Bad Request if token is missing
        return "Bad Request: 'token' is required", 400
        
    if data["token"] != "secret-123":
        # Return 401 Unauthorized if token is incorrect
        return "Unauthorized: Invalid token", 401
        
    return "Verification Successful!", 200
```

---

## Notes

- **HTTP Status Code Defaults**: If you do not specify a status code in your return tuple (e.g. you return just a string), Flask defaults to `200 OK`.
- **405 Handling**: If a user makes a request to a route using a method not defined in the `methods` list (e.g. sending a `PUT` to `/api/verify` from Example 3), Flask will automatically reply with a `405 Method Not Allowed` response.

---

## Summary

- REST APIs use resources identified by URIs and standard HTTP methods to represent actions.
- `GET` is safe and idempotent. `POST` is neither. `PUT` and `DELETE` are idempotent but not safe.
- Status codes communicate the result of an HTTP request (2xx for success, 4xx for client errors, 5xx for server errors).

---

## Practice Exercises

1. Design the REST URI endpoints and HTTP methods required for a student grading system where you need to:
   - List all student grades.
   - Fetch the grade of a student named `"Snehal"`.
   - Submit a new grade.
   - Change an existing grade.
   - Delete a student grade profile.
2. Write a Flask route `/api/items` that handles `GET`, `POST`, and `DELETE` requests. Return a different string and appropriate status code for each method.
3. Write a Flask route `/api/divide` that parses two query parameters `a` and `b`. If either is missing, return a `400` status code. If `b` is zero, return a `400` status code. Otherwise, return the division result and a `200` status.

---

## Further Reading

- [Architectural Styles and the Design of Network-based Software Architectures (REST)](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
- [MDN Web Docs: HTTP Request Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [MDN Web Docs: HTTP Response Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
