# Threading

**Course:** Automation using Python — Part 1  
**Module 12:** Parallel Execution in Python

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Explain what threads are in Python
- Identify I/O-bound tasks that benefit from threading
- Create and start threads in simple scripts
- Understand basic thread coordination concepts

---

## Introduction

Threading allows a program to work on multiple tasks that can make progress during waiting periods, such as file access, network calls, or API requests. In automation, threading is often useful for I/O-bound tasks where the script spends time waiting on external operations.

---

## Key Concepts

### What a thread is

A thread is a unit of execution within a process. Multiple threads can exist in one Python program.

### When threading helps

Threading is often helpful for:

- downloading multiple files
- calling several APIs
- waiting on network responses
- reading from many slow sources

### I/O-bound vs CPU-bound

Threading is usually more effective for **I/O-bound** work than for heavy **CPU-bound** computation in standard Python.

### Basic thread lifecycle

Typical steps:

1. define a target function
2. create a thread
3. start the thread
4. join the thread if you need to wait for completion

---

## Examples

### Example 1: Start one thread

```python
import threading

def say_hello():
    print("Hello from thread")

thread = threading.Thread(target=say_hello)
thread.start()
thread.join()
```

### Example 2: Start multiple threads

```python
import threading
import time

def worker(name):
    print(f"Starting {name}")
    time.sleep(1)
    print(f"Finished {name}")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(f"task-{i}",))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
```

### Example 3: Threading for simulated waiting

```python
import threading
import time

def fetch_data(source):
    print(f"Fetching from {source}")
    time.sleep(2)
    print(f"Done with {source}")

for source in ["api1", "api2"]:
    threading.Thread(target=fetch_data, args=(source,)).start()
```

---

## Notes

- Use threading mainly for tasks that wait on I/O.
- Always think about shared state when multiple threads run together.
- Use `join()` when the main program must wait for completion.
- Keep threaded tasks small and independent when possible.

---

## Summary

- Threading allows multiple tasks to make progress during waiting periods.
- It is especially useful for I/O-bound automation work.
- Good threaded code keeps tasks simple and coordinates completion clearly.

---

## Practice Exercises

1. Create a thread that prints a message after a short delay.
2. Launch three worker threads and wait for all of them to finish.
3. List two automation tasks that are good candidates for threading.

---

## Further Reading

- [threading documentation](https://docs.python.org/3/library/threading.html)
