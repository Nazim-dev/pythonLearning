from turtle import Turtle, update
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font= FONT)

    def win(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font= FONT)