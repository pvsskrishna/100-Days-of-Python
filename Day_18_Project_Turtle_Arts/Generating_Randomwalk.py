import random
import turtle
from turtle import Turtle,Screen

screen = Screen()
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

tim = Turtle()
angle = [0,90,180,270]
tim.pensize(10)
tim.speed(0)

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b


def walk(walk_range):
    for _ in range(walk_range):
        tim.pencolor(random_color())
        tim.forward(30)
        tim.setheading(random.choice(angle))

walk(1000)

screen.exitonclick()