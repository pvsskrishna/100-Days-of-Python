# 💌 Day 24 - Mail Merge Project: Auto-Generate Invitation Letters

This project is a classic **Mail Merge** automation tool. 📬  
It reads a list of names from a file, customizes a letter template for each recipient, and writes the personalized messages into new files — all with Python!

---

## 🚀 Project Name: Mail Merge – Auto Invitation Letter Generator

This project is designed to simulate a common real-world automation task: sending personalized messages at scale using templates.  
Perfect for events, emails, or mass communication.

---

## 🧠 Features Implemented

✅ Reads recipient names from a `.txt` file  
✅ Uses a placeholder-based letter template  
✅ Automatically replaces `[name]` with the actual name  
✅ Generates separate, cleanly formatted invitation letters  
✅ Stores output in a designated `Output` folder

---

## 📁 Folder Structure

```
Day_24_Project_Mail_Merge
│
├── Input
│   ├── Letters
│   │   └── starting_letter.txt
│   └── Names
│       └── invited_names.txt
│
├── Output
│   └── ReadyToSend
│       ├── Letter_for_Amarendra Bahubali.txt
│       ├── Letter_for_Zoro.txt
│       ├── Letter_for_Tanjiro.txt
│       ├── Letter_for_Kattappa.txt
│       ├── Letter_for_Shraddha.txt
│       ├── Letter_for_Dhoni.txt
│       ├── Letter_for_Uncle Iron man.txt
│       └── Letter_for_Tata.txt
│
└── main.py
```

---

## 🔧 How It Works

1. The script reads all names from `invited_names.txt`.
2. It reads the content from `starting_letter.txt` which contains a placeholder `[name]`.
3. It loops through each name, replaces `[name]` with the actual name, and writes a new file inside the `ReadyToSend` folder.

---

## 🗂️ Files and Their Roles

| File/Folder                       | Description                                 |
|----------------------------------|---------------------------------------------|
| `main.py`                        | Main logic for reading, merging, and writing|
| `starting_letter.txt`            | Template letter with placeholder `[name]`   |
| `invited_names.txt`              | List of names to send letters to            |
| `ReadyToSend/`                   | Output folder containing all final letters  |

---

## 📌 Sample Output

For example, for the name **Zoro**, this letter gets generated:

```
Dear Zoro,

You are invited to my birthday this Saturday.

Hope you can make it!

Varun
```

---

## 💡 Fun Fact

The idea of **mail merge** goes way back to early word processors in the 1980s, where office workers would automate form letters using address databases.  
With Python, the same power is in your hands with just a few lines of code! ⚡🐍

---

## 🔗 GitHub Repo

👉 Check out the full code here:  
[https://github.com/pvsskrishna/100-Days-of-Python/tree/main/Day_24_Project_Mail_Merge](#)

---

Let's keep building and automating with Python! 🚀  
See you on **Day 25**!

#100DaysOfCode #Python #Automation #MailMerge #TextProcessing #Day24 #CodeNewbie
