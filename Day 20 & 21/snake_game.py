from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

"""Creates screen"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

"""Creates snake and food"""
snake = Snake()
food = Food()
scoreboard = Scoreboard()

"""Controls"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Food collision detection
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    #Self collision
    for part in snake.snake_parts:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 5:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()