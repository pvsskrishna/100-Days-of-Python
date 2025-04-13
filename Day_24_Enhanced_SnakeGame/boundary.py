from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(-320, 220)  # Starting position (Top Left)
        self.pendown()
        self.draw_boundary()

    def draw_boundary(self):
        self.goto(320,220)
        self.goto(320,-220)
        self.goto(-320,-220)
        self.goto(-320,220)
