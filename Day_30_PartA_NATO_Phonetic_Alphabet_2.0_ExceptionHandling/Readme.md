# 🔤 Day 30 – Part A: NATO Phonetic Alphabet Project 2.0 (with Exception Handling)

This project is an enhanced version of my Day 26 **NATO Phonetic Alphabet Converter**, now improved with **exception handling** to make it more robust and user-friendly.

---

## 🧠 Project Overview

The program converts any English word input by the user into its corresponding NATO phonetic alphabet representation.

For example:  
**Input:** `Varun`  
**Output:** `['Victor', 'Alfa', 'Romeo', 'Uniform', 'November']`

---

## ✅ What’s New in Version 2.0

| Feature | Old Version (Day 26) | New Version (Day 30 - Part A) |
|--------|------------------------|-------------------------------|
| 📦 File Structure | `main.py`, `nato_phonetic_alphabet.csv` | `ExceptionHandling_in_NATO_Phonetic_Alphabet_Project.py`, `nato_phonetic_alphabet.csv` |
| 🛠 Error Handling | ❌ No validation for non-alphabet characters | ✅ Now handles invalid inputs using `try-except` block |
| 🔁 Retry Mechanism | ❌ Crashes on invalid input | ✅ Prompts user again for valid input |
| 🧼 Clean Output | ❌ Printed both dict and list output | ✅ Prints only the required phonetic list |
| 🔄 Recursive Input | ❌ One-time input only | ✅ Recursively asks for new input until valid |

---

## 📂 Project Files

- `ExceptionHandling_in_NATO_Phonetic_Alphabet_Project.py` – Enhanced version with input validation
- `main.py` – Original implementation from Day 26 (for comparison)
- `nato_phonetic_alphabet.csv` – Dataset containing NATO alphabet

---

## 💡 Key Enhancements

✔️ Wrapped the list comprehension in a `try-except` block to catch `KeyError`  
✔️ Handles invalid characters like digits or symbols gracefully  
✔️ Recursively calls the function again to allow user retry  
✔️ Converts input to uppercase automatically to ensure matching with dataset

---

## 🧰 Concepts Used

- Python `pandas` for reading CSV data  
- Dictionary comprehension to build the phonetic dictionary  
- Exception Handling using `try`, `except`, `else`  
- Input validation and recursive function calls

---

## 🚀 How to Run

1. Ensure `pandas` is installed:  
   ```bash
   pip install pandas
   ```

2. Run the improved version:  
   ```bash
   python ExceptionHandling_in_NATO_Phonetic_Alphabet_Project.py
   ```

3. Enter an English word. If you enter invalid characters (like digits or punctuation), you’ll be prompted again!

---

## 🤓 Fun Fact

The NATO phonetic alphabet was designed to reduce errors in transmission — just like this program now reduces input errors through exception handling!

---

## 🏁 Summary

This upgraded version focuses on **real-world usability**. It was fun revisiting my older code and applying exception handling to create a smoother user experience.

📌 Stay tuned for **Part B: Password Manager 2.0**!
