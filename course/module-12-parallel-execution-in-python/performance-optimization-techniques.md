# Performance optimization techniques

**Course:** Automation using Python — Part 1  
**Module 12:** Parallel Execution in Python

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Identify common performance bottlenecks in automation scripts
- Apply simple optimization techniques before adding complexity
- Measure script behavior to guide improvement decisions
- Choose appropriate performance strategies for different workloads

---

## Introduction

Not every slow script needs threads or processes. Many performance problems come from inefficient file handling, repeated computations, unnecessary loops, or slow external calls. Good optimization starts with measurement and simple improvements.

---

## Key Concepts

### Find the bottleneck first

Before optimizing, determine what is actually slow:

- file I/O
- network calls
- database queries
- repeated computations
- inefficient data transformations

### Simple optimizations

Useful low-complexity improvements include:

- reducing repeated work
- caching reusable values
- processing data in batches
- avoiding unnecessary file reads or writes
- using efficient libraries for tabular data

### Measure execution time

Use timing tools or simple timestamps to compare approaches.

### Optimize responsibly

A faster script is not better if it becomes unreliable or impossible to understand.

---

## Examples

### Example 1: Measure execution time

```python
import time

start = time.time()
time.sleep(1)
end = time.time()

print(f"Elapsed time: {end - start:.2f} seconds")
```

### Example 2: Avoid repeated computation

```python
numbers = [1, 2, 3, 4]
squares = [n * n for n in numbers]
print(squares)
```

### Example 3: Process data in chunks conceptually

```python
rows = list(range(1, 11))
chunk_size = 3
for i in range(0, len(rows), chunk_size):
    print(rows[i:i + chunk_size])
```

---

## Notes

- Measure before and after optimization.
- Prefer simple wins before advanced concurrency.
- Reduce unnecessary I/O when possible.
- Keep correctness and readability as priorities.

---

## Summary

- Optimization should begin with understanding the bottleneck.
- Many automation scripts can be improved with simple changes.
- Performance work should be guided by measurement, not guesswork.

---

## Practice Exercises

1. Measure the execution time of a short Python operation.
2. Describe two non-concurrency ways to speed up an automation script.
3. Explain why optimization without measurement is risky.

---

## Further Reading

- [time module documentation](https://docs.python.org/3/library/time.html)
- [timeit documentation](https://docs.python.org/3/library/timeit.html)
