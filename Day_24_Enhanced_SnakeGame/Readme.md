# 🐍 Day 24 - Snake Game Part 3: Enhanced & Smarter Snake Game

Welcome to **Day 24** of my [#100DaysOfPython](https://www.linkedin.com/feed/hashtag/100daysofpython/) journey!  
Today’s focus was on **enhancing** the Snake Game I built on Day 21, turning it into a **smarter**, more engaging version with added functionality and a better user experience. 🎮✨

---

## 🚀 Project Name: Snake Game Part 3 – Enhanced Classic Edition

This version builds directly on **Day 21's Snake Game** and introduces **major improvements** that add polish, persistence, and challenge to the gameplay experience.

---

## 🔑 Key Enhancements from Day 21

| Feature | Day 21 | Day 24 |
|--------|--------|--------|
| 🟡 **Food Color** | Blue | Yellow |
| 🧠 **Game Over** | Game ends on collision | Game resets automatically |
| 🏆 **High Score Tracking** | Not implemented | High Score saved to `data.txt` |
| ♻️ **Snake Reset** | Not available | Snake resets position & state |
| ✨ **UI Update** | Static Score | Displays `Score` + `High Score` |
| 🧽 **Clean Handling** | Basic restart logic | Fully resets snake & scoreboard |

---

## 🧠 Features Implemented

✅ Snake movement using arrow keys  
✅ Random food generation (yellow)  
✅ Snake grows on eating food  
✅ Live Score + Persistent High Score  
✅ Collision detection with wall and tail  
✅ Auto-reset on collision instead of Game Over screen  
✅ Game boundary drawing with Turtle  

---

## 🕹️ How It Works

- Use **Arrow Keys** to control the snake.  
- Eat the **yellow food** to grow and increase your score.  
- The game now **auto-resets** when the snake hits a wall or itself.  
- **High Score** is stored and retained using `data.txt`.  
- Beat your own high score every time you play!

---

## 🗂️ Files and Their Roles

| File Name       | Role Description |
|----------------|------------------|
| `main.py`      | Main game loop and controls |
| `snake.py`     | Snake movement, growth, and reset logic |
| `food.py`      | Handles food generation (yellow!) |
| `scoreboard.py`| Displays live score and tracks high score |
| `boundary.py`  | Draws red boundary using Turtle |
| `data.txt`     | Stores persistent high score data |

---

## 🧑‍💻 Concepts Covered

- Object-Oriented Programming (OOP) in Python  
- Keyboard event binding with `onkey()`  
- File handling for high score tracking (`read`/`write`)  
- Collision detection using `distance()`  
- Game screen updating using `tracer()` and `update()`  
- Resetting objects dynamically during gameplay  

---

## 💡 Fun Fact

> In early versions of Snake, hitting a wall meant **Game Over**. In this version, your snake **revives and restarts**, giving you a second chance — but your high score will keep haunting you until you beat it! 😄

---

## 🔗 GitHub Repo

👉 Check out the full enhanced code here:  
https://github.com/pvsskrishna/100-Days-of-Python/tree/main/Day_24_Enhanced_SnakeGame

---

Stay tuned for more improvements and creative builds as I continue exploring the world of Python! 🐍🚀  
Let’s keep coding and make learning fun! 🎯

---

**#100DaysOfCode #Python #TurtleGraphics #SnakeGame #GameDevelopment #CodeNewbie #Day24 #LearnByBuilding**
