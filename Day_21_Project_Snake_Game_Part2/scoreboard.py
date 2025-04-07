# TODO:5 Create score board
from turtle import Turtle
ALIGNMENT = "center"
FONT_STYLE = ("arial", 20, "bold")
MOVE_TEXT = False



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0,220)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}", move=MOVE_TEXT, align=ALIGNMENT, font=FONT_STYLE)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=MOVE_TEXT, align=ALIGNMENT, font=FONT_STYLE)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



