from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.x_move = 6
        self.create_car()

    def create_car(self):
        y = random.randint(-240, 260)
        self.shape("square")
        self.shapesize(1.3, 3)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(300, y)


    def drive(self):
        x = self.xcor() - self.x_move
        self.setx(x)
