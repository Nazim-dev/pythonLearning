import time
from turtle import Screen, onkey, speed
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

traffic = []
l = 6

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_speed = 0.1

player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()

    if l % 6 == 0:
        car = CarManager()
        traffic.append(car)

    l += 1

    for cars in traffic:
        cars.drive()
        if cars.distance(player) < 27:
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.win()
        player.reset()
        car_speed *= 0.9

scoreboard.game_over()
screen.exitonclick()