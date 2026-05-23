# Interacting with desktop applications

**Course:** Automation using Python — Part 1  
**Module 8:** GUI Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Structure automation steps for desktop applications
- Use screen coordinates, windows, and application states carefully
- Understand simple strategies for finding UI elements
- Reduce failures caused by timing or interface changes

---

## Introduction

Desktop application automation means using Python to complete tasks inside installed software such as internal tools, spreadsheets, or legacy business systems. The challenge is not just sending clicks and keystrokes, but doing so at the right place and time.

---

## Key Concepts

### Build a predictable workflow

A reliable desktop automation script usually follows a sequence like this:

1. open the application
2. wait for the window to load
3. focus the correct window or field
4. perform input steps
5. confirm the result

### Coordinate-based interaction

Some GUI scripts interact with fixed screen coordinates. This is simple but fragile if the window moves or screen resolution changes.

### Image-based interaction

Some tools can locate buttons or fields from screenshots. This is often more flexible than fixed coordinates, but it can still fail if themes or layouts change.

### Confirm application state

Before typing or clicking, confirm the correct application is open and ready. This reduces the risk of entering data in the wrong place.

---

## Examples

### Example 1: Plan a desktop automation sequence

```python
workflow = [
    "Launch the application",
    "Wait for login screen",
    "Enter username and password",
    "Open the claims screen",
    "Type the claim number",
    "Save the result"
]

for step in workflow:
    print(step)
```

### Example 2: Pause before interacting

```python
import time

print("Waiting for the application window...")
time.sleep(3)
print("Now continue")
```

### Example 3: Validate state with a screenshot search concept

```python
status = "button found"
if status == "button found":
    print("Safe to continue")
else:
    print("Stop and review the screen")
```

---

## Notes

- Keep workflows short and focused when starting out.
- Add checks between important steps.
- Avoid running desktop automation in the background while also using the same machine.
- If available, use window controls or application APIs instead of raw screen coordinates.

---

## Summary

- Desktop automation requires both user-like actions and careful state management.
- Reliable workflows depend on timing, focus, and predictable screen layout.
- Short, validated steps are safer than long blind click sequences.

---

## Practice Exercises

1. Write a step-by-step plan for automating a simple form in a desktop app.
2. List two risks of coordinate-based interaction.
3. Explain why confirming application state matters before typing.

---

## Further Reading

- [PyAutoGUI screenshot functions](https://pyautogui.readthedocs.io/en/latest/screenshot.html)
