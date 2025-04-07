import time
from turtle import Turtle,Screen
from boundary import Boundary
from snake import Snake
from food import Food
from scoreboard import Scoreboard

"""Setup"""
screen = Screen()
screen.setup(width=700,height=500)
screen.bgcolor("black")
screen.title("Snake_Game")
screen.tracer(0)

#TODO: Draw Boundary
boundary = Boundary()


#TODO:1 Create snake body
snake = Snake("square","white")

#TODO:3 Create Snake Food
food = Food()
score = Scoreboard()

#TODO:2 Move the snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #TODO:4 Detect collision with food + Increase the length of snake
    if snake.head.distance(food) < 15:
        # TODO:5 Create score board
        score.increase_score()
        snake.extend()
        food.refresh()

    #TODO:6 Detect collision with wall
    if snake.head.xcor() < -320 or snake.head.xcor() > 320 or snake.head.ycor() < -220 or snake.head.ycor() > 220:
        game_is_on = False
        print("Game over")
        score.game_over()

    #TODO:7 Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()