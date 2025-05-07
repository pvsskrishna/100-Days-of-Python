# Day 28: Pomodoro Timer with Tkinter GUI


## 🚀 Project Name
**Pomodoro Timer with GUI**

## 🧠 What is the Pomodoro Technique?
The **Pomodoro Technique** is a time management method developed by Francesco Cirillo in the late 1980s. It uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

This method helps boost productivity by encouraging focused work and timely breaks.

---

## 🛠️ What I Developed

### ✅ Main Features
- A fully functional **Pomodoro timer** with GUI.
- **25-minute** work sessions.
- **5-minute** short breaks after each session.
- **20-minute** long break after every 4 Pomodoros.
- **Start**, **Reset**, and countdown functionality.
- Visual checkmarks (`✔`) to indicate completed sessions.

### 💻 Technologies Used
- `Tkinter` for GUI development
- `time` module for countdown
- Functions for managing states (work/break cycles)

---

## 📂 Project Structure

- `main.py` – This is the core of the application. It contains:
  - Timer constants and global variables
  - The UI setup using `Tkinter` canvas, labels, and buttons
  - Timer logic using `after()` method of Tkinter for non-blocking countdown
  - Reset and start button functionality
  - Visual indicators like ticks for completed Pomodoros

---

## 🧪 How to Run

1. Make sure you have Python installed.
2. Run the file:
   ```bash
   python main.py
   ```
3. A window will appear with the Pomodoro Timer. Click "Start" to begin!

---

## 🔍 Concepts Practiced & Learned

- Tkinter UI components: `Canvas`, `Button`, `Label`, `PhotoImage`
- Using the `.after()` method for scheduling callbacks
- State management and logic flow for repetitive cycles
- Visual feedback with dynamic UI updates

---

## 🤓 Fun Fact

The name “Pomodoro” comes from the **tomato-shaped kitchen timer** that Cirillo used as a university student! 🍅

---

## 📸 Preview

The timer starts counting down with a tomato image, showing "Work" or "Break", and checkmarks appear as you complete sessions.

---

