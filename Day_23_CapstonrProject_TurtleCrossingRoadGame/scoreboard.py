FONT = ("Courier",24,'normal')

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,150)
        self.level = 1


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over",align="center",font=FONT)

    def hurray(self):
        self.goto(0, 0)
        self.write("Hurray",align="center",font=FONT)

    def display_level(self,level):
        self.clear()
        self.goto(-290, 150)
        self.write(f"Level: {self.level}", align="left", font=FONT)

