from turtle import Turtle,Screen
screen = Screen()
screen.screensize()
screen.setup(width = 1.0, height = 1.0)
tim = Turtle()

def draw_dashed_line():
    for _ in range(25):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

draw_dashed_line()


screen.exitonclick()