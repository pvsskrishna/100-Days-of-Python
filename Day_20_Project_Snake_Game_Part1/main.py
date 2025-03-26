import time
from turtle import Turtle,Screen
from snake import Snake

"""Setup"""
screen = Screen()
screen.setup(width=700,height=500)
screen.bgcolor("black")
screen.title("Snake_Game")
screen.tracer(0)

#TODO:1 Create snake body
snake = Snake("square","white")


#TODO:2 Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

#TODO:3 Create Snake Food
#TODO:4 Detect collision with food + Increase the length of snake
#TODO:5 Create score board
#TODO:6 Detect collision with wall
#TODO:7 Detect collision with tail

screen.exitonclick()