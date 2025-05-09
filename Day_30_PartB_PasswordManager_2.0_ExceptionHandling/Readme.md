# 🔐 Day 30 - Part B: Advanced Password Manager with JSON Storage

Welcome to **Day 30 - Part B**
In this part, I upgraded the basic password manager from **Part A (Day 29)** to store login credentials in a **JSON file** and added search functionality — making it more robust, scalable, and user-friendly. 💾🗃️

---

## 🧠 Project Overview

This project expands upon the Day 29 text-based password manager by:
- Migrating from plain text to structured JSON format
- Allowing users to **search** for credentials by website name
- Handling missing or corrupted files gracefully

---

## ✅ What’s New in Version 2.0

| Feature                            | Old Version (Day 29)              | New Version (Day 30 - Part B)          |
|------------------------------------|-----------------------------------|----------------------------------------|
| 🗃️ Data Storage                     | Plain text (`save_data.txt`)      | Structured JSON (`data.json`)          |
| 🔍 Search Functionality             | ❌ Not available                   | ✅ Find credentials by website name     |
| 💾 Data Persistence                 | Appends text to file              | Merges & updates key-value pairs       |
| 🛡 Error Handling                   | ❌ None                            | ✅ Graceful handling of missing/corrupt files |
| 📋 Auto-Copy Password               | ✅ Yes                             | ✅ Yes (unchanged)                      |

---

## 📂 Project Files

- `main.py` – Full-featured password manager GUI with JSON storage and search
- `data.json` – Stores login credentials for each website in key-value format
- `logo.png` – Lock icon used in the tkinter GUI

---

## 🔑 Key Features

✔️ Generate secure passwords with letters, numbers, and symbols  
✔️ Save credentials for websites in `data.json`  
✔️ Auto-copy passwords to clipboard  
✔️ Retrieve stored credentials with search functionality  
✔️ Exception handling for empty input fields, missing JSON file, and malformed data

---

## 🧰 Concepts Used

- GUI with `tkinter`  
- File handling with `json.load`, `json.dump`, `try/except` blocks  
- Dynamic data updates using Python dictionaries  
- Clipboard interaction via `pyperclip`  
- Grid layout management in `tkinter`

---

## 🚀 How to Run

1. Ensure required libraries are installed:  
   ```bash
   pip install pyperclip
   ```

2. Run the application:  
   ```bash
   python main.py
   ```

3. Use the interface to generate and manage passwords securely.

---

## 💡 Fun Fact

Unlike flat `.txt` files, **JSON** provides a structured format that scales with your application. It’s human-readable, easy to update, and ideal for small-scale data storage in apps like this one.

---

## 🏁 Summary

Part B turns the password manager into a **fully functional personal vault**, complete with search capabilities and data persistence. A small but powerful step into real-world app development! 🔐

📌 [GitHub Repository](https://github.com/pvsskrishna/100-Days-of-Python/tree/main/Day_30_PartB_Password_Manager)
