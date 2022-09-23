STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT= 0

from shutil import move
from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.up()
            snake.goto(pos)
            self.snake_parts.append(snake)

    def move(self):
        for snake_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[snake_num - 1].xcor()
            new_y = self.snake_parts[snake_num - 1].ycor()
            self.snake_parts[snake_num].goto(new_x, new_y)
        self.head.fd(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)