# Automating mouse and keyboard actions

**Course:** Automation using Python — Part 1  
**Module 8:** GUI Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Use Python to move the mouse and simulate clicks
- Send keyboard input and shortcuts programmatically
- Add delays to make GUI automation more reliable
- Use fail-safe practices while testing automation scripts

---

## Introduction

The most direct form of GUI automation is controlling the mouse and keyboard. Libraries such as `pyautogui` can simulate actions that a human user performs on screen.

This approach is powerful, but it should be tested carefully because incorrect clicks or keystrokes can affect the wrong window.

---

## Key Concepts

### Common mouse actions

A GUI automation script may:

- move to screen coordinates
- click or double-click
- drag items
- scroll

### Common keyboard actions

A script may:

- type text
- press individual keys
- send keyboard shortcuts
- navigate between fields using `Tab` or `Enter`

### Timing and pauses

Applications may need time to respond. Adding small delays improves stability.

### Fail-safe behavior

Tools like `pyautogui` support a fail-safe feature so rapid mouse movement to a screen corner stops the script. This is important for safe testing.

---

## Examples

### Example 1: Move and click with `pyautogui`

```python
import pyautogui

pyautogui.moveTo(500, 300, duration=0.5)
pyautogui.click()
```

### Example 2: Type text and press Enter

```python
import pyautogui

pyautogui.write("POLICY-10025", interval=0.05)
pyautogui.press("enter")
```

### Example 3: Use delays between actions

```python
import pyautogui
import time

pyautogui.click(400, 250)
time.sleep(1)
pyautogui.write("Daily report")
```

---

## Notes

- Install the library with `pip install pyautogui` before running examples.
- Test with non-critical applications first.
- Keep the target window visible and stable.
- Use small pauses and fail-safe settings to reduce mistakes.

---

## Summary

- Mouse and keyboard automation is a core part of GUI scripting.
- `pyautogui` can simulate many user actions quickly.
- Safe timing and testing practices are essential for reliable execution.

---

## Practice Exercises

1. Write a script that waits briefly, then types a short message.
2. Move the mouse to a position and click once.
3. Simulate typing text followed by pressing `Enter`.

---

## Further Reading

- [PyAutoGUI mouse functions](https://pyautogui.readthedocs.io/en/latest/mouse.html)
- [PyAutoGUI keyboard functions](https://pyautogui.readthedocs.io/en/latest/keyboard.html)
