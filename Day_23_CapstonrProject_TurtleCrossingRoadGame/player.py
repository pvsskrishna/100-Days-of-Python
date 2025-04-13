
MOVE_PLAYER_DISTANCE = 10
STARTING_POSITION = (0,-180)
FINISHING_LINE_Y = 180

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("turtle")
        self.color("black")
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        if self.ycor() < 180:
            self.forward(MOVE_PLAYER_DISTANCE)

    def is_at_finishline(self):
        if self.ycor() >= FINISHING_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)