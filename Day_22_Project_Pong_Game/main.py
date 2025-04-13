#TODO 1: Create the Screen
#TODO 2: Create and Move Paddle
#TODO 3: Create another Paddle
#TODO 4: Create the ball and make it move
#TODO 5: Detect collision with wall and bounce
#TODO 6: Detect collision with paddle
#TODO 7: Detect when paddle misses
#TODO 8: Keep score

import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

TITLE = "Pong Game"
BG_COLOR = "Black"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

turtle = Turtle()
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT,startx=0,starty=0)
screen.bgcolor(BG_COLOR)
screen.title(TITLE)

left_paddle = Paddle((-350,0)) # here position we are passing as tuple: position =(x,y)
right_paddle = Paddle((350,0))

screen.listen()
screen.onkeypress(left_paddle.go_up,"w")
screen.onkeypress(left_paddle.go_down,"s")

screen.onkeypress(right_paddle.go_up,"Up")
screen.onkeypress(right_paddle.go_down,"Down")

game_is_on = True
while game_is_on:
    ball.move_ball()
    time.sleep(ball.move_speed)
    screen.update()

    #Detect the collision with upper walls
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    #Detect collision with paddle
    if (ball.xcor() > 320 and ball.distance(right_paddle) < 50 and ball.x_move > 0) or \
            (ball.xcor() < -320 and ball.distance(left_paddle) < 50 and ball.x_move < 0):
        ball.bounce_x()


    #Detect R paddle misses
    if ball.xcor() > 370:
        scoreboard.l_point()
        ball.reset_position()

    #Detect L paddle misses
    if ball.xcor() < -370:
        scoreboard.r_point()
        ball.reset_position()




screen.exitonclick()