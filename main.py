import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, 'w')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    for car in cars.all_cars:

        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        player.go_to_start()
        cars.next_level()
        score.increase_score()

screen.exitonclick()
