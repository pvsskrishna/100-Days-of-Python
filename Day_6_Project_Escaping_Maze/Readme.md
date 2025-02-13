# Escaping the Maze 🏃‍♂️🌀

## Project Overview
The **Escaping the Maze** project is a Python-based solution for navigating a maze in **Reeborg’s World**, an online programming tool for learning Python through robotics simulation. The objective is to guide Reeborg (the robot) through a maze until it reaches the goal using basic programming logic and control flow.

## How It Works
1. **Reeborg starts at a random position inside the maze** and must find the exit.
2. The robot follows a **wall-following algorithm** (right-hand rule) to navigate efficiently.
3. The program checks for possible moves using built-in functions:
   - `front_is_clear()` → Move forward if no obstacle.
   - `right_is_clear()` → Turn right if possible.
   - `wall_on_right()` → Keep following the wall to the right.
   - `at_goal()` → Stop when the goal is reached.
4. The robot moves through a **while loop** until it escapes the maze.

## Python Concepts Used
- **Loops** (`while not at_goal()`) → Ensures continuous movement until the goal is reached.
- **Conditional Statements** (`if-elif-else`) → Determines the next move based on obstacles.
- **Functions** (`def turn_right()`, `def jump()`) → Enhances code reusability.
- **Logical Operators** (`and`, `or`, `not`) → Used for decision-making in navigation.

## How to Run the Program
1. Open **[Reeborg’s World](https://reeborg.ca/reeborg.html)**.
2. Select the **Maze Escape Challenge** from the available worlds.
3. Copy and paste the following code into the editor:
   ```python
   def turn_right():
       turn_left()
       turn_left()
       turn_left()
       
   def jump():
       turn_left()
       while wall_on_right():
           move()
       turn_right()
       move()
       turn_right()
       while front_is_clear():
           move()
       turn_left()
       
   while not at_goal():
       if right_is_clear():
           turn_right()
           move()
       elif front_is_clear():
           move()
       else:
           turn_left()
   ```
4. Click **Run** and watch Reeborg escape the maze! 🎉

## Have fun coding! 🚀

