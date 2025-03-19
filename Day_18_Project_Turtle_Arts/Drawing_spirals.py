from turtle import Turtle, Screen
import turtle as t
import random

screen = Screen()
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

tim = Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

tim.pensize(2)
tim.speed("fastest")

def draw_spirals(size_of_gap):
    current_heading = tim.heading()
    for _ in range(360//size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        current_heading += size_of_gap
        tim.setheading(current_heading)

draw_spirals(5)
screen.exitonclick()