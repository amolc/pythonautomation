# Multiprocessing for parallel execution

**Course:** Automation using Python — Part 1  
**Module 12:** Parallel Execution in Python

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Explain what multiprocessing is
- Recognize CPU-bound tasks that benefit from separate processes
- Create worker processes in Python
- Understand the tradeoffs of process-based parallelism

---

## Introduction

Multiprocessing runs work in separate processes instead of separate threads. This is useful for CPU-heavy tasks because each process has its own Python interpreter and memory space. In automation, multiprocessing can help when many independent calculations or transformations must be performed.

---

## Key Concepts

### What multiprocessing means

A process is an independent running program instance. Multiple processes can run in parallel on different CPU cores.

### When multiprocessing helps

Multiprocessing is often a better choice for:

- image transformations
- large data calculations
- CPU-heavy parsing
- expensive batch processing tasks

### Process pools

The `multiprocessing.Pool` class makes it easier to distribute work across multiple processes.

### Costs and tradeoffs

Multiprocessing adds overhead:

- more memory use
- more startup cost
- more complex data sharing

It should be used when the performance benefit justifies that complexity.

---

## Examples

### Example 1: Start one process

```python
from multiprocessing import Process

def worker():
    print("Running in a separate process")

process = Process(target=worker)
process.start()
process.join()
```

### Example 2: Use a process pool

```python
from multiprocessing import Pool

def square(number):
    return number * number

with Pool(processes=2) as pool:
    results = pool.map(square, [1, 2, 3, 4])

print(results)
```

### Example 3: Compare independent tasks

```python
tasks = ["resize image", "compress file", "analyze dataset"]
for task in tasks:
    print(f"Independent task: {task}")
```

---

## Notes

- Multiprocessing is best for CPU-bound work.
- Keep tasks independent to reduce data-sharing complexity.
- Measure performance before assuming multiprocessing is necessary.
- On some platforms, process startup behavior requires careful script structure.

---

## Summary

- Multiprocessing uses separate processes to achieve true parallel execution for CPU-bound work.
- It is useful when independent tasks need significant computation.
- The benefits must be weighed against extra complexity and overhead.

---

## Practice Exercises

1. Create a script that starts one worker process.
2. Use a process pool to apply a function to a list of numbers.
3. Name two automation tasks that are better suited to multiprocessing than threading.

---

## Further Reading

- [multiprocessing documentation](https://docs.python.org/3/library/multiprocessing.html)
