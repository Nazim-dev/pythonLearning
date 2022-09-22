from turtle import Turtle, Screen

koopa = Turtle()
screen = Screen()

def move_forward():
    koopa.fd(10)

def move_backward():
    koopa.bk(10)

def turn_left():
    koopa.left(-10)

def turn_right():
    koopa.right(10)

def clear_screen():
    koopa.clear()
    koopa.up()
    koopa.home()
    koopa.down()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)



screen.exitonclick()