import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed =  MOVE_INCREMENT

    def create_car(self):
        random_number = random.randint(0, 6)
        if random_number == 6:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shape("car.gif")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car_y = random.choice(list(range(200, -251, -60)))
            new_car.goto(300, new_car_y)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
