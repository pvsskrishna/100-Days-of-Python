# ✉️ Day 32 – Part A: Friday Motivation Mail Sender

## 📌 Project Overview
This project sends a **random motivational quote** every **Friday** to a specified email address. It's a great way to lift spirits and help people start their weekend on a positive note. 🧠

It’s the first part of a two-part automation system using **Python + smtplib**. The second part (coming up) handles **birthday wish automation**.

---

## 💡 How It Works
📅 Every time the script runs:
- It checks if **today is Friday** using the `datetime` module.
- If it is Friday:
  - It reads a list of motivational quotes from `quotes.txt`.
  - Picks a random quote.
  - Sends the quote to the target email using Gmail's SMTP server via **smtplib**.

---

## 📚 Concepts Used

📌 Python Libraries:
- `smtplib` — for sending emails securely using Gmail's SMTP server  
- `datetime` — to check the current day of the week  
- `random` — for selecting a random quote  
- `email.message.EmailMessage` — for structured email formatting

💡 Programming Concepts:
- Working with external `.txt` files  
- Email authentication & TLS encryption  
- Random quote selection logic  
- Conditional execution based on weekday

---

## 📁 Project Files

- `Friday_Motivation_Project_main.py` → Main script for Friday emails  
- `quotes.txt` → A list of motivational quotes (hundreds of them!)  
- `resource_docs.txt` → Reference links for Python modules used  

---

## 🚀 How to Run

1. Make sure you have Python 3.10+ installed.
2. Install necessary libraries (if not already available):
   ```bash
   pip install secure-smtplib
   ```
3. Replace the `my_gmail`, `password`, and `msg["To"]` fields in the code with your credentials and recipient's address.
4. Run the script any day of the week — it will only send emails **on Friday**.

---

## 🔐 Security Tip
Always store email credentials securely. In production, **use environment variables** or **.env files** instead of hardcoding them.

---

## 📎 Resources Used

- Python `smtplib` docs → [Email SMTP Docs](https://docs.python.org/3/library/smtplib.html)  
- Python `datetime` docs → [Datetime Docs](https://docs.python.org/3.12/library/datetime.html#datetime.datetime)  
- Quote sources → [Positivity Blog Quotes](https://www.positivityblog.com/monday-motivation-quotes/)

---

## 🤖 Fun Fact
This script is **PythonAnywhere-ready** — meaning you can deploy and schedule it to run every Friday *automatically* from the cloud. Set it and forget it! 😎
