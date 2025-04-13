#TODO 1: Move turtle from bottom to top using keypress
#TODO 2: Create and Move Cars from Right to left
#TODO 3: Detect Collision with car
#TODO 4: Detect the when turtle reaches otherside
#TODO 5: Create and Update a scoreboard

from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=400)
screen.tracer(0)
screen.title("Cross the Road")

player = Player()
car = CarManager()
scoreboard = Scoreboard()
scoreboard.display_level(level=scoreboard.level)

screen.listen()
screen.onkeypress(player.move_up,'w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    #Detect collision with cars
    for vehicle in car.all_cars:
        if vehicle.distance(player) < 22:
            scoreboard.game_over()
            game_is_on = False

        #Detect the successful crossing road
        elif player.is_at_finishline():
            player.go_to_start()
            car.level_up()
            scoreboard.level += 1
            scoreboard.display_level(level=scoreboard.level )








screen.exitonclick()