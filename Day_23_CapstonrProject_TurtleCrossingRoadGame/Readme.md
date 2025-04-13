# 🐢 Day 23 - Cross the Road Game

Welcome to **Day 23** of my #100DaysOfPython journey! 🎯  
Today, I built a fun arcade-style **Cross the Road** game using **Python Turtle Graphics** — inspired by the classic *Frogger* game.

---

## 🚀 Project Name: Cross the Road - Turtle vs Traffic

This game challenges players to navigate a turtle safely across a road while avoiding oncoming cars.  
With every successful crossing, the game speeds up — testing your timing and reflexes! 💥🐢

---

## 🎮 How It Works

- You control a turtle using the `W` key to move up
- Randomly colored cars appear from the right and move to the left
- Avoid the cars — collision ends the game
- Reach the top of the screen to level up
- With each level, cars move faster!

---

## 🧩 Project Structure

```bash
.
├── main.py           # Game loop and overall game management
├── player.py         # Turtle player movement and reset logic
├── car_manager.py    # Car creation, movement, and speed control
└── scoreboard.py     # Level tracking and Game Over display
```
---
## 📌 Concepts Covered

- ✅ Object-Oriented Programming (OOP)
- ✅ Inheritance and Turtle class extension
- ✅ Collision detection using .distance()
- ✅ Dynamic difficulty with speed scaling
- ✅ Event-driven programming with onkeypress()
- ✅ Real-time screen updates with tracer() and update()

## ▶️ How to Run the Game
1. Clone this repository or download the files
2. Ensure Python is installed on your system
3. Open terminal or command prompt and run:

```bash
cd /path/to/Cross_the_Road
python main.py
```
4. Use the W key to move the turtle upward and avoid the traffic!

---

## 💡 Fun Fact
This game is inspired by the legendary Frogger arcade game from 1981 🐸
It was so popular, it made appearances in Seinfeld and Wreck-It Ralph — now, it lives on in Python with a brave little turtle! 🐢🚧


