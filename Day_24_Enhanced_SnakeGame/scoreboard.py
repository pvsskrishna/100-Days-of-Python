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

        with open("data.txt",mode = "r") as data:
            self.highscore = int(data.read())

        self.color("white")
        self.goto(0,220)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score} Highscore = {self.highscore}", move=MOVE_TEXT, align=ALIGNMENT, font=FONT_STYLE)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.writing_highscore_data()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", move=MOVE_TEXT, align=ALIGNMENT, font=FONT_STYLE)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

    def writing_highscore_data(self):
        with open("data.txt", mode="w") as data:
            data.write(f"{self.highscore}")




