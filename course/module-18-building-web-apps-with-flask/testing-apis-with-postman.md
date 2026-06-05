# Testing APIs with Postman

**Course:** Automation using Python — Part 1  
**Module 18:** Building Web Apps with Flask

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Explain what Postman is and how it helps verify API functionality.
- Import a pre-configured JSON collection file into Postman.
- Manage and apply Postman environments and variables.
- Run complete HTTP request testing sequences (GET, POST, PUT, DELETE) on your local Flask server.

---

## Introduction

Once you have written your Flask API, you need a way to test it. While writing a Python script using the `requests` library is a great approach for automation, it can be slow for manual testing and prototyping. 

**Postman** is a popular, free API client interface that allows developers to construct, save, send, and test HTTP requests. Rather than typing complex `curl` commands in the terminal, Postman provides a visual interface for entering request bodies, setting headers, inspecting status codes, and verifying JSON responses.

---

## Key Concepts

### What is a Postman Collection?

A **Collection** in Postman is a group of pre-configured HTTP requests that are saved together. Instead of rebuilding requests (setting headers, query params, and body data) every time, you can group them by feature area or project. You can save, export, and share collections as JSON files.

### Variables and Environments

In production, your API might run on `https://api.mycompany.com`. In development, it runs on `http://127.0.0.1:5000`. 

To avoid updating the URL inside dozens of saved requests, Postman allows you to define an **Environment** containing variables. For example, you can create a variable named `base_url` and write your request paths as:
`{{base_url}}/api/products`

When you switch your active environment in Postman, `{{base_url}}` automatically resolves to the correct host.

---

## Examples

### Example 1: Importing a Collection

To import the collection file provided in this module (`postman-collection.json`):
1. Open the Postman application.
2. In the top-left corner, click the **Import** button.
3. Drag and drop the `postman-collection.json` file into the upload box.
4. Click **Import** to confirm. A new collection folder named `Module 18: Flask Inventory API` will appear in your sidebar.

### Example 2: Configuring Environment Variables

To set up a local development environment:
1. Click on the **Environments** tab on the left sidebar in Postman.
2. Click the **+** (Create Environment) button and name it `Flask Local`.
3. Add a new variable:
   - **Variable**: `base_url`
   - **Type**: `default`
   - **Initial Value**: `http://127.0.0.1:5000`
   - **Current Value**: `http://127.0.0.1:5000`
4. Click **Save** in the top-right corner.
5. Set the active environment in the top-right dropdown selector to `Flask Local`.

Now, any request referencing `{{base_url}}` will target your local Flask server.

### Example 3: Running the CRUD Verification Sequence

With your Chapter 6 Flask app running (`python app.py`), execute the following requests in order:

1. **GET All Products**:
   - Send `GET {{base_url}}/api/products`.
   - Verify it returns a `200 OK` status and an empty JSON array `[]` (if the database is new).
2. **POST Create Product**:
   - Select the `Create Product` request. Notice the headers include `Content-Type: application/json`.
   - The body contains:
     ```json
     {
       "name": "Wireless Mouse",
       "price": 29.99,
       "stock": 50
     }
     ```
   - Send the request. Verify it returns `201 Created` with the product dictionary including `"id": 1`.
3. **GET Single Product**:
   - Send `GET {{base_url}}/api/products/1`.
   - Verify it returns `200 OK` and details for the "Wireless Mouse".
4. **PUT Update Product**:
   - Select `Update Product` targeting `{{base_url}}/api/products/1`.
   - Update the body to change stock to `45`:
     ```json
     {
       "name": "Wireless Mouse",
       "price": 29.99,
       "stock": 45
     }
     ```
   - Send request. Verify it returns the updated object with stock `45`.
5. **DELETE Product**:
   - Send `DELETE {{base_url}}/api/products/1`.
   - Verify it returns `200 OK` and a success message.
6. **GET Deleted Product (Verification)**:
   - Send `GET {{base_url}}/api/products/1` again.
   - Verify the server returns a `404 Not Found` status code and `{"error": "Product not found"}` JSON.

---

## Notes

- **Payload Format**: If your POST or PUT requests return a `400 Bad Request` or fail to parse variables on the Flask side, check that your Postman request body type is set to **raw** and the format dropdown is set to **JSON** (which adds the critical `Content-Type: application/json` header).
- **Postman Tests Tab**: You can write JavaScript assertions inside the **Tests** tab of any request. For example:
  ```javascript
  pm.test("Status code is 201", function () {
      pm.response.to.have.status(201);
  });
  ```
  This is highly useful for automating API validation.

---

## Summary

- Postman helps build, organize, and test HTTP request endpoints in a visual dashboard.
- Collections organize related requests and can be imported/exported as JSON files.
- Environment variables (`{{variable_name}}`) allow you to change API targets dynamically.
- Verifying an API involves running sequence assertions (Create -> Read -> Update -> Delete -> Verify 404).

---

## Practice Exercises

1. Create a new environment in Postman named `Flask Staging` and set `base_url` to `http://127.0.0.1:8080`. Toggle between `Flask Local` and `Flask Staging` to see the request URLs change dynamically.
2. In the `GET All Products` request, add a query parameter `name` with value `Mouse`. Send the request and check the query console to verify it translates to `{{base_url}}/api/products?name=Mouse`.
3. Open the `Create Product` request, click on the **Tests** tab, and add a test to verify that the returned JSON contains the property `id`. Run the request to confirm the test passes.

---

## Further Reading

- [Postman Learning Center: Introduction to Collections](https://learning.postman.com/docs/sending-requests/intro-to-collections/)
- [Postman Learning Center: Using Variables](https://learning.postman.com/docs/sending-requests/variables/)
- [Postman Learning Center: Test Scripts](https://learning.postman.com/docs/writing-scripts/intro-to-scripts/)
