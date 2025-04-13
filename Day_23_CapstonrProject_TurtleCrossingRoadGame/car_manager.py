import random
import time
COLORS = ["violet","indigo","blue","green","yellow","orange","red"]
STARTING_POSITION_X = 300
MOVE_CAR_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = MOVE_CAR_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,8)
        if random_chance == 6:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            car_y = random.randint(-150,150)
            new_car.goto(STARTING_POSITION_X, car_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


