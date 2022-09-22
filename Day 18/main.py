# import colorgram

# colors = colorgram.extract('C:/Users/sense/Desktop/Python/100 days of code/Day 18/spots.jpg' , 8)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)

from turtle import Screen, Turtle
import random

koopa = Turtle()
screen = Screen()
color_list = [(220, 229, 233), (237, 227, 233), (187, 38, 59), (240, 213, 48), (249, 160, 58), (45, 96, 164)]

screen.colormode(255)
koopa.up()
counter = 0
move_up = 35
koopa.setposition(-250 , 0)

while counter < 101:
    for i in range(10):
        koopa.fd(50)
        koopa.pencolor(random.choice(color_list))
        koopa.dot(20)
        counter += 1
    koopa.setposition(-250, move_up)
    move_up += 35

screen.exitonclick()