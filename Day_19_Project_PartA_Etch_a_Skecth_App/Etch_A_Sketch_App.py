#Python_HighOrderFunctions_&_KeyEventListeners
from turtle import Turtle,Screen
tim=Turtle()
screen = Screen()
screen.setup(1.0,1.0)

def move_forward():
    # tim.setheading(0)
    tim.forward(10)

def move_backward():
    # tim.setheading(180)
    tim.backward(10)

def right_curve():
    # tim.circle(-30, 30)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def left_curve():
    #tim.circle(30, 30)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=right_curve,key="d")
screen.onkey(fun=left_curve,key="a")
screen.onkey(fun=clear,key="c")


screen.exitonclick()