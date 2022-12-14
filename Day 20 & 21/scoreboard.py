from turtle import Turtle, color

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", color="black", align="center", font=("Arial", 15, "normal"))
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER \nScore: {self.score}", align="center", font=("Arial", 15, "normal"))
    

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    