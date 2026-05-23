# Introduction to task scheduling

**Course:** Automation using Python — Part 1  
**Module 10:** Task Scheduling and Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Define task scheduling in an automation context
- Explain why automation jobs are often scheduled instead of run manually
- Identify common recurring workflows that benefit from scheduling
- Understand the role of timing, frequency, and reliability

---

## Introduction

Writing a useful automation script is only part of the solution. In many real workflows, the script must also run at the right time: every morning, every hour, once per week, or after a specific event. Task scheduling allows automation to happen without manual triggering.

---

## Key Concepts

### What task scheduling means

Task scheduling means configuring a script or command to run automatically at a chosen time or interval.

Examples:

- generate a daily report at 8:00 AM
- archive logs every night
- check a folder every 15 minutes
- send reminders every Monday

### Why scheduling matters

Scheduling helps automation become dependable and routine. It reduces the need for human memory and ensures repeated work happens on time.

### Common scheduling decisions

When planning a scheduled job, think about:

- how often it should run
- what inputs must exist before it starts
- where output should be stored
- how to know whether it succeeded or failed

### Scheduled automation needs visibility

A scheduled script may run with no human watching it, so logs, output files, and clear error handling are important.

---

## Examples

### Example 1: Common scheduling ideas

```python
jobs = [
    "Daily branch report at 08:00",
    "Weekly backup on Sunday",
    "Folder check every 15 minutes"
]

for job in jobs:
    print(job)
```

### Example 2: Represent a simple schedule in code

```python
schedule_info = {
    "task": "Send daily summary",
    "frequency": "daily",
    "time": "08:00"
}

print(schedule_info)
```

### Example 3: Why logs matter

```python
print("A scheduled task should leave evidence that it ran")
```

---

## Notes

- Schedule only scripts that can run unattended.
- Make input and output paths predictable.
- Add logs or status files so success is visible.
- Start with simple schedules before building more complex chains.

---

## Summary

- Task scheduling runs automation scripts at planned times or intervals.
- Scheduling is essential for recurring operational workflows.
- Reliable scheduled tasks need good timing, logging, and error handling.

---

## Practice Exercises

1. List three tasks that are good candidates for scheduling.
2. Explain why logs are important for scheduled automation.
3. Describe one daily script that should run automatically in a business workflow.

---

## Further Reading

- [cron on Wikipedia](https://en.wikipedia.org/wiki/Cron)
- [Windows Task Scheduler overview](https://learn.microsoft.com/windows/win32/taskschd/task-scheduler-start-page)
