# 🏓 Day 22 - Pong Game

Welcome to **Day 22** of my #100DaysOfPython journey! 🎯
Today, I recreated the iconic **Pong Game** using **Python Turtle Graphics**. It’s a fully interactive two-player game featuring ball mechanics, paddle control, scoring, and collision detection.

---

## 🚀 Project Name: Pong Game - Classic Arcade Remake

This game simulates the classic **Pong arcade experience**, featuring:
- Two-player paddle control (W/S and Up/Down keys)
- A bouncing ball with increasing speed
- Dynamic scoreboard updates
- Ball resets and win tracking

---

## 🎮 How It Works

- Each player controls a vertical paddle:
  - **Left Player:** `W` (up) and `S` (down)
  - **Right Player:** `↑` (up) and `↓` (down)
- The ball bounces off top/bottom walls and paddles.
- A player scores when the opponent misses the ball.
- First to score more points wins!

---

## 🧩 Project Structure

```bash
.
├── main.py         # Main game loop and key bindings
├── ball.py         # Ball movement, bounce logic, and resets
├── paddle.py       # Paddle movement and initialization
└── scoreboard.py   # Tracks and displays player scores
```

---

## 📌 Concepts Covered

✅ Object-Oriented Programming (OOP)  
✅ Inheritance using Turtle graphics  
✅ Real-time collision detection  
✅ Game loop and frame-based control with `tracer()` and `update()`  
✅ Keyboard event handling using `onkeypress()`  

---

## ▶️ How to Run the Game

1. Clone the repository or download the files
2. Make sure Python is installed
3. Open terminal or command prompt:
   ```bash
   cd /path/to/Pong_Game
   python main.py
   ```
4. Use keyboard keys to control paddles and have fun! 🏓

---

## 💡 Fun Fact

The original **Pong** was released by Atari in 1972. It’s widely regarded as the **first commercially successful video game**, and it sparked the arcade gaming industry as we know it today! 🕹️🧠

---

Stay tuned for Day 23 where I’ll be diving into more advanced game logic and projects!
Let’s keep coding and learning — one day at a time. 💪🐍

