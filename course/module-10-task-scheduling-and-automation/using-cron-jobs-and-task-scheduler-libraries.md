# Using cron jobs and task scheduler libraries

**Course:** Automation using Python — Part 1  
**Module 10:** Task Scheduling and Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Understand how cron jobs schedule commands on Unix-like systems
- Recognize the role of Windows Task Scheduler
- Use Python scheduler libraries for in-process timing
- Choose an appropriate scheduling tool for a given task

---

## Introduction

There are several ways to schedule automation tasks. Some schedules are managed by the operating system, while others are handled by Python libraries. Choosing the right tool depends on where the script runs and how the workflow should be managed.

---

## Key Concepts

### Cron jobs

`cron` is a scheduler commonly used on Linux and macOS. It runs commands at specified times using cron expressions.

Example cron entry:

```bash
0 8 * * * /usr/bin/python3 /path/to/daily_report.py
```

This runs the script every day at 8:00 AM.

### Windows Task Scheduler

On Windows, Task Scheduler provides similar functionality through a graphical interface or command-line tools.

### Python scheduler libraries

Some libraries schedule jobs inside a running Python process.

Examples:

- `schedule`
- `APScheduler`

These are useful when you want scheduling logic in Python code, but they still need a running process or service.

### Choosing between them

- Use OS schedulers for stable system-level jobs.
- Use Python scheduler libraries when scheduling rules belong inside the application.
- Keep the solution as simple as possible.

---

## Examples

### Example 1: Cron expression

```bash
30 9 * * 1-5 /usr/bin/python3 /path/to/check_claims.py
```

This runs at 9:30 AM on weekdays.

### Example 2: Use the `schedule` library

```python
import schedule
import time

def job():
    print("Running scheduled task")

schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

### Example 3: A simple scheduled function idea

```python
def generate_report():
    print("Report generated")
```

---

## Notes

- Install the `schedule` library with `pip install schedule` if you want to use it.
- Cron and Task Scheduler are better for jobs that must run even when your script is not already running.
- Use full paths in scheduler configurations to avoid path-related failures.
- Test the command manually before scheduling it.

---

## Summary

- Cron and Task Scheduler are operating-system tools for scheduled execution.
- Python libraries such as `schedule` support in-code scheduling.
- The right scheduler depends on environment, reliability needs, and simplicity.

---

## Practice Exercises

1. Explain what the cron entry `0 6 * * * script.py` is intended to represent.
2. Write a small `schedule` example that prints a message every minute.
3. Compare one advantage of OS-level scheduling with one advantage of a Python scheduler library.

---

## Further Reading

- [schedule documentation](https://schedule.readthedocs.io/)
- [APScheduler documentation](https://apscheduler.readthedocs.io/)
