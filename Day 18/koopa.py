from turtle import Turtle, Screen

koopa = Turtle()

screen = Screen()

koopa.shape("turtle")
koopa.color("SpringGreen3")

# koopa.fd(100)
# koopa.left(90)
# koopa.fd(100)
# koopa.left(90)
# koopa.fd(100)
# koopa.left(90)
# koopa.fd(100)

# for x in range(20):
#     koopa.fd(10)
#     koopa.up()
#     koopa.fd(10)
#     koopa.down()

# for x in range(3):
#     koopa.fd(100)
#     koopa.left(120)

# koopa.color("aquamarine")
# for x in range(4):
#     koopa.fd(100)
#     koopa.left(90)

# koopa.color("brown")
# for x in range(5):
#     koopa.fd(100)
#     koopa.left(72)

# koopa.color("blue")
# for x in range(6):
#     koopa.fd(100)
#     koopa.left(60)

# koopa.color("BlueViolet")
# for x in range(7):
#     koopa.fd(100)
#     koopa.left(51.43)

# koopa.color("DarkOrange")
# for x in range(8):
#     koopa.fd(100)
#     koopa.left(45)

# koopa.color("DarkSeaGreen")
# for x in range(9):
#     koopa.fd(100)
#     koopa.left(40)

# koopa.color("DarkSlateGrey")
# for x in range(10):
#     koopa.fd(100)
#     koopa.left(36)

import random

koopa.width(10)
koopa.speed(10)
directions = [0, 90, 180, 270]

for i in range (200):
    koopa.forward(30)
    koopa.setheading(random.choice(directions))


screen.exitonclick()