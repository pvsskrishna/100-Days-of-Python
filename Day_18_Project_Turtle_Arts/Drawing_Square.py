from turtle import Turtle,Screen

screen = Screen()
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

tim = Turtle()
def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

draw_square()

screen.exitonclick()