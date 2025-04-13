from turtle import Turtle,Screen
FONT = ("Courier",80,'normal')
ALIGN = "center"
L_SCORE_POSITION = (-100,200)
R_SCORE_POSITION = (100,200)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(L_SCORE_POSITION)
        self.write(self.l_score,align=ALIGN,font=FONT)
        self.goto(R_SCORE_POSITION)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

