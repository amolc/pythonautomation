# Automating recurring tasks and processes

**Course:** Automation using Python — Part 1  
**Module 10:** Task Scheduling and Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Design recurring automation workflows with clear inputs and outputs
- Add logging and simple reliability checks to scheduled jobs
- Identify common recurring tasks in operations and reporting
- Think about monitoring and recovery for unattended scripts

---

## Introduction

Recurring tasks are one of the biggest opportunities in automation. If a job happens every day, every week, or every month, it is often worth turning into a scheduled process. The goal is not just to run code on a schedule, but to create a workflow that consistently produces the expected result.

---

## Key Concepts

### Common recurring automation tasks

Examples include:

- daily report generation
- weekly data backups
- hourly folder monitoring
- monthly reconciliation summaries
- recurring email notifications

### Think beyond the script

A recurring process should define:

- where the input comes from
- where the output goes
- what happens if input is missing
- how success or failure is recorded

### Logging and monitoring

A scheduled workflow should produce a log, status message, or output file that confirms it ran.

### Failure handling

Unattended tasks may fail because of missing files, network issues, permission problems, or code errors. Even simple checks can make automation more reliable.

---

## Examples

### Example 1: Basic recurring task idea

```python
def daily_summary():
    print("Generate summary, save file, write log")
```

### Example 2: Simple logging pattern

```python
from datetime import datetime

with open("run.log", "a", encoding="utf-8") as file:
    file.write(f"[{datetime.now().isoformat(timespec='seconds')}] Task ran\n")
```

### Example 3: Check for a required input file

```python
from pathlib import Path

input_file = Path("input/daily.csv")
if input_file.exists():
    print("Process input file")
else:
    print("Input missing; stop and log the issue")
```

---

## Notes

- Recurring automation should be predictable and easy to verify.
- Logs, timestamps, and output folders make troubleshooting easier.
- Handle missing input gracefully instead of failing silently.
- Keep scheduled workflows small and modular when possible.

---

## Summary

- Recurring tasks are strong candidates for automation.
- Good scheduled workflows define timing, inputs, outputs, and failure behavior.
- Logging and simple validation make unattended jobs much easier to manage.

---

## Practice Exercises

1. Design a daily automation workflow with one input, one output, and one log file.
2. Add a file existence check before processing a recurring input.
3. Explain two things you would monitor in a scheduled reporting job.

---

## Further Reading

- [logging documentation](https://docs.python.org/3/library/logging.html)
- [pathlib documentation](https://docs.python.org/3/library/pathlib.html)
