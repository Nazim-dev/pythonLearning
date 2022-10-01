from os import stat
import turtle
import pandas

data = pandas.read_csv("Day 25/us-states-game/50_states.csv")
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []


while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Name a State").title()

    if answer == "Exit":
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{answer}", align="center", font= ("Courier", 10, "normal"))

#states missed csv

for state in guessed_states:
    all_states.remove(state)

states_df = pandas.DataFrame(all_states)

states_df.to_csv("Day 25/us-states-game/states_missed.csv")

screen.exitonclick()

