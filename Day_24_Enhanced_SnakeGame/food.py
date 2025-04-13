
import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("yellow")
        self.speed("fast")
        # self.refresh()

    # TODO:4 Detect collision with food
    def refresh(self):
        random_x = random.randint(-310 , 310)
        random_y = random.randint(-210, 210)
        self.goto(random_x, random_y)



