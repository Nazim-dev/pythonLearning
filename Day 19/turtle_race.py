from turtle import Turtle, Screen
import random

is_race_started = False
screen = Screen()
screen.setup(width=500, height=400)
y_axis = -130
user_choice = screen.textinput(title="Choose a turtle", prompt="Which turtle will win the race? ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
# koopa = Turtle(shape="turtle")
# koopa.up()
# koopa.goto(x=-230, y=y_axis)

for turtle in colors:
    color = turtle
    turtle = Turtle(shape="turtle")
    turtle.up()
    turtle.color(color)
    y_axis += 40
    turtle.goto(x=-230, y=y_axis)
    turtle_list.append(turtle)

if user_choice:
    is_race_started = True

while is_race_started:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_started = False
            winner = turtle.pencolor()
            if winner == user_choice:
                print(f"You won, {winner} finished first")
            else:
                print(f"You lost, {winner} finished first")
        distance = random.randint(0, 15)
        turtle.forward(distance)



screen.exitonclick()