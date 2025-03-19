import turtle
import random
from turtle import *

screen = Screen()
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

tim = Turtle()

tim.pensize(0)
tim.speed(1)
tim.penup()
tim.goto(0,100)
tim.pendown()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    tim.color(random_color())
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

for sides in range(3,11):
    draw_shape(sides)


screen.exitonclick()
