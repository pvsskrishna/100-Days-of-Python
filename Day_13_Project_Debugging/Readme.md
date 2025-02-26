# Debugging Challenges - Day 13 🐞

## Project Overview

Day 13 is not just another coding day—it’s **Debugging Day!** 🛠️ Today’s challenge is all about fixing broken code and understanding **why** it didn’t work in the first place. Debugging is an essential skill for any programmer, and learning how to identify and fix errors can save hours of frustration.

### What’s Special About Today’s Challenge? 🎯

Each exercise follows a structured approach:
✅ A **buggy code snippet** 🫅
✅ **Requirements & rules** 🗒️
✅ The **issues found** 🔍
✅ The **fixed version** 🛠️
✅ Key **findings & takeaways** 💡

Debugging isn’t just about fixing errors—it’s about understanding **why** they happen and learning from them!

---

## 1⃣ Debugging Odd or Even 🟢

### 📌 Requirement:

- Write a function that takes a number as input.
- It should return **"This is an even number."** if the number is even.
- Otherwise, return **"This is an odd number."**

### 🚩 Buggy Code:

```python
def odd_or_even(number):
    if number % 2 = 0:
        return "This is an even number."
    else:
        return "This is an odd number."
```

### 🔥 Issues Found:

- `=` is an **assignment operator**, but we need `==` for comparison.
- This causes a **syntax error**.

### ✅ Fixed Code:

```python
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
```

### 🔍 Findings & Takeaways:

✔️ Always use **==** for comparison, not **=**.
✔️ Debugging starts with reading error messages!
✔️ Even numbers are divisible by 2 without a remainder.

---

## 2⃣ Debugging Leap Year 🗓️

### 📌 Requirement:

A year is a **leap year** if:

1. It is **divisible by 4**.
2. But **not divisible by 100**, unless it is also **divisible by 400**.

### 🚩 Buggy Code:

```python
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
```

### 🔥 Issues Found:

- `4000` should be `400` based on leap year rules.
- The incorrect condition leads to wrong outputs.

### ✅ Fixed Code:

```python
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

is_leap(2000)
```

### 🔍 Findings & Takeaways:

✔️ Always check **mathematical logic** carefully.
✔️ Test cases help find errors in conditions.
✔️ Leap years follow a **special rule** beyond just divisibility by 4.

---

## 3⃣ Debugging FizzBuzz 🎮

### 📌 Requirement:

Print numbers from **1 to X**, but:

- If a number is **divisible by 3**, print "Fizz".
- If a number is **divisible by 5**, print "Buzz".
- If a number is **divisible by both 3 and 5**, print "FizzBuzz".
- Otherwise, print the number itself.

### 🚩 Buggy Code:

```python
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0:
            print("Fizz")
          elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")        
        else:
            print(number)

fizz_buzz(25)
```

### 🔥 Issues Found:

- The `elif` for checking **both 3 and 5** should come first!
- Incorrect indentation for `elif` caused **SyntaxError**.
- Checking **3 before 3 & 5** skips "FizzBuzz" logic.

### ✅ Fixed Code:

```python
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz(25)
```

### 🔍 Findings & Takeaways:

✔️ **Order matters** in conditional checks.
✔️ Fix **indentation issues** to avoid SyntaxErrors.
✔️ **FizzBuzz is a classic coding test question!**

---

## 🏆 Summary

Debugging is a crucial skill for developers. Today, we:

- **Fixed syntax errors** (wrong operators, missing indentations).
- **Checked data types** (converting input to integer).
- **Followed logical order** in conditions.
- Learned how **small mistakes** can break a program!

🚀 Keep debugging, keep learning! Happy coding!

