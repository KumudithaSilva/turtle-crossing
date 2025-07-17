import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# TODO 1. Move the turtle with key press
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    # TODO 2. Create and move the cars
    car_manager.create_car()
    car_manager.move_cars()
    screen.update()

    # TODO 3. Detect collision with cars
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # TODO 4. Detect when the turtle reached to other side
    if player.ycor() > 280:
        # TODO 5. Create scoreboard
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        car_manager.level_up()
        player.goto(STARTING_POSITION)

screen.exitonclick()
