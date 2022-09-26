from turtle import Turtle

x_pos = 350
y_pos = 0
p_width = 5
p_height = 1

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(pos)
        self.shapesize(p_width, p_height)
        
        
        
    def move_up(self):
         new_y = self.ycor() + 20
         self.goto(self.xcor(), new_y)

    def move_down(self):
         new_y = self.ycor() - 20
         self.goto(self.xcor(), new_y)
        