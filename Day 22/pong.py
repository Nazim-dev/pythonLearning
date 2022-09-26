from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.move_up,"Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up,"w")
screen.onkey(paddle2.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Paddle collision
    if ball.distance(paddle1) < 50 and ball.xcor() > 330 or ball.distance(paddle2) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Paddle miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.player1()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.player2()

screen.exitonclick()