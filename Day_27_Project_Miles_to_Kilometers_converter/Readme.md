
# 📘 Day 27 - Unit Converter with GUI

## 📌 Project Title: `Unit Converter with GUI (Tkinter)`

---

### 🧠 About the Project

This project showcases a **Unit Converter** GUI built using Python’s built-in **Tkinter** library. The main functionality is in the `main.py` file, which allows users to convert distances from **miles to kilometers** via an interactive graphical interface.

This project not only implements the actual converter, but also explores and experiments with a wide range of **Tkinter widgets** in two supporting files: `Concept.py` and `Other_Tkinter_Widgets.py`.

Together, this project serves two purposes:
1. 🚀 A **functional app** – the Unit Converter
2. 🧪 A **sandbox for learning** – demonstration of all major widgets and layout techniques in Tkinter

---

### 🖥 What Does `main.py` Do?

- Provides a clean and minimal **Unit Converter GUI**.
- Takes **miles as input** from the user.
- On clicking the **"Calculate"** button, it converts miles to kilometers using the formula:  
  `km = miles × 1.609`
- Displays the result dynamically in the GUI.
- Demonstrates how to:
  - Use labels and entry fields
  - Bind buttons to callback functions
  - Format layout using `grid()`
  - Update widgets dynamically using `.config()`

---

### 🎯 Additional Learning in `Concept.py` and `Other_Tkinter_Widgets.py`

#### 🔍 `Concept.py`:
- Focuses on the `grid()` layout system.
- Shows how to create:
  - Labels
  - Buttons
  - Entry widgets
- Demonstrates how to configure spacing, minimum size, and dynamic updates using `.config()` and `.get()`.

#### 🧪 `Other_Tkinter_Widgets.py`:
- Demonstrates a wide range of widgets:
  - `Text`, `Spinbox`, `Scale`
  - `Checkbutton`, `Radiobutton`, `Listbox`
- Teaches interaction using `command` callbacks and `.bind()` methods.
- Covers concepts like using `IntVar()` and getting current values from widgets.
- Uses the `pack()` geometry manager to arrange widgets vertically.

---

### 🧰 Concepts Used

- `Tkinter` library
- GUI layout managers: `grid()` and `pack()`
- Labels, Entries, and Buttons
- Text widgets
- Checkbuttons, Radiobuttons, and Scales
- `Spinbox` and `Listbox`
- `IntVar()` and event handling via `command` and `bind`
- String manipulation and formatting
- Unit conversion math logic

---

### 📚 Concepts Learned

- How to structure GUI applications
- Reading and updating input fields
- Updating widget text dynamically
- Organizing layouts using `padx`, `pady`, `columnspan`, `sticky`, and `minsize`
- Handling widget states and user interaction events

---

### 🧪 Fun Facts

- You can update label text dynamically using `.config(text="new value")`.
- Mixing `grid()` and `pack()` in the same container widget (like a Frame) will cause errors.
- `Entry.get()` reads text input as a string – always cast to `float` or `int` when doing calculations.
- `Text` widgets require special handling to get content using `.get("1.0", "end-1c")`.

---

### 🚀 How to Run

1. Ensure **Python 3.x** is installed on your system.
2. Save the files:
   - `main.py` (Unit Converter)
   - `Concept.py` (Grid layout demo)
   - `Other_Tkinter_Widgets.py` (Widget experiments)
3. Run them separately using:
   ```bash
   python main.py
   python Concept.py
   python Other_Tkinter_Widgets.py
   ```

---

### 🖼️ Preview

Here’s what you can expect from `main.py`:

```
[ Miles ]     miles
    ↓
[ Calculate ] → [ km output ]
```

User enters miles, clicks calculate, and gets the result in kilometers.

---

### 📦 Files Included

- `main.py` → ✅ Unit Converter GUI (Miles → Kilometers)
- `Concept.py` → 📐 Grid layout demo with entry/label/button
- `Other_Tkinter_Widgets.py` → 🎛 Widget playground (checkboxes, sliders, etc.)

---

### 🏁 Status

✅ Completed – GUI-based unit converter built with extended Tkinter practice sessions!

---

### 🧑‍💻 Author

Varun S10048  
Day 27 – #100DaysOfPython challenge  
Odin School – DS47 Batch
