# 🧠 Day 31: Language Flash Cards (Telugu-English) with Tkinter

Today’s project is a visual language learning tool using **Python + Tkinter** that helps users memorize Telugu-English word pairs using a digital **flash card system**.

---

## 🗂️ Project Name
**Telugu-English Language Flash Cards**

---

## 🧩 Project Overview

The flash card app helps users learn Telugu vocabulary by flipping cards that show a word in Telugu and then reveal its English meaning after a 3-second delay.

Users can mark words they already know, which removes them from the learning list for future sessions. It’s a smart way to build long-term memory!

---

## 💡 Key Features

✅ Displays Telugu word first, auto-flips to English after 3 seconds  
✅ Uses `Tkinter Canvas` for front/back card switching  
✅ Saves progress using `words_to_learn.csv`  
✅ User clicks ✅ or ❌ to navigate and save known words  
✅ Automatically loads the remaining words on next session  
✅ Gracefully handles missing save files (with `try-except` block)

---

## 📁 File Structure

- `main.py` → Core logic and UI for the flash card app  
- `Telugu_English_Freq - Sheet1.csv` → Initial vocabulary list  
- `words_to_learn.csv` → Auto-generated file storing user progress  
- `images/` → Card front/back images + right/wrong icons  
- `Sources.txt` → References for vocabulary and translation data

---

## 📚 Concepts Used

✔ GUI layout with Tkinter  
✔ `Canvas` and `PhotoImage` for visual cards  
✔ Reading/writing CSV files with pandas  
✔ Dictionary and list manipulation  
✔ Timer callbacks using `window.after()`  
✔ Error handling for missing files

---

## 🚀 How to Run

1. Make sure `pandas` is installed:
```bash
pip install pandas
```

2. Ensure images are in the correct `images` directory (`card_front_compact.png`, `card_back_compact.png`, `right.png`, `wrong.png`)

3. Run the app:
```bash
python main.py
```

4. Click ✅ to move to the next word, ❌ if the word is known and should be removed from the review list.

---

## 🌍 Source Data Credits

Data sources for words and frequency lists:  
- Wiktionary Frequency Lists  
- Hermit Dave's FrequencyWords GitHub  
- Google Translate APIs  
- OpenSubtitles Corpus  
- [Google Sheet - English Telugu High Frequency Words](https://docs.google.com/spreadsheets/d/1nm-6J9G4HNAxYHRuV4J4HgNtKi3N32h-Lu0u93z8egQ/edit?gid=0#gid=0)

(Full list in `Sources.txt`)

---

## 🤓 Fun Fact

Did you know? Studies show that **active recall** (like using flashcards) is one of the most effective ways to learn a new language. This app is built on that exact principle!

---

## ✅ Summary

This was a fun and interactive project that blends UI design with smart logic for spaced repetition. A powerful step forward for visual learners and language enthusiasts!
