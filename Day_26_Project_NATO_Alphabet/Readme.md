# 📦 Day 26: NATO Phonetic Alphabet Converter

This Python project is a simple but powerful tool that converts any word into the NATO phonetic alphabet using the `pandas` library.

## 🧠 What You Will Learn

- Reading CSV files with `pandas`
- Creating dictionaries from data frames
- Using dictionary and list comprehensions
- Handling user input and mapping it to data
- Exception handling for invalid entries

---

## 📁 Project Structure

```
📦 Day26_NATO_Alphabet
├── 📄 main.py
├── 📄 concept.py
├── 📄 nato_phonetic_alphabet.csv
```

- `main.py` — Core logic to convert any word into phonetic alphabet.
- `concept.py` — A sandbox to experiment with dictionary and list comprehensions.
- `nato_phonetic_alphabet.csv` — Contains mappings for A-Z to their NATO equivalents.

---

## 🚀 How It Works

1. Load the CSV into a DataFrame using pandas.
2. Create a dictionary mapping each letter to its phonetic code.
3. Prompt the user for input.
4. Convert each letter to its corresponding code and print the result.

### 💡 Sample Output:

```
Enter a word: Hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

---

## 🧪 Example Use Case

Input: `Python`  
Output: `['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']`

---

## ✅ Requirements

- Python 3.x
- pandas

You can install pandas using pip if not already installed:

```bash
pip install pandas
```

---

## 💡 Fun Fact

The NATO Phonetic Alphabet was developed to ensure clear communication—especially over radio or telephone—where mishearing letters can be costly. Even today, it's used in aviation, military, and emergency services worldwide.

---

Happy coding! 🚀
