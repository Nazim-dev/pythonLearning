from turtle import Turtle, Screen
from prettytable import PrettyTable

# koopa = Turtle()

# koopa.shape("turtle")
# koopa.color("blue")
# koopa.pencolor("black")

# koopa.forward(100)

# new_screen = Screen()
# new_screen.exitonclick()

table = PrettyTable()
table.align = "l"
table.field_names = ["Game", "Genre"]
table.add_row(["Battlefield", "Shooter"])
table.add_row(["Grid", "Racing"])
table.add_row(["Super Mario", "Platformer"])


print(table)