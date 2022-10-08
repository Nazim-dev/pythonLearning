from cProfile import label
from cgitb import text
from random import randint
from textwrap import fill
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LABEL_COLOR = "#FFFFFF"
CARD_COLOR = "#91C2AF"
FRENCH_COLOR = "#000000"
card = {}
card_words = {}

try:
    data = pandas.read_csv("Day 31/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("Day 31/data/french_words.csv")
    card_words = data.to_dict(orient="records")
else:
    card_words = data.to_dict(orient="records")


#Get card
def get_word():
    global card, switch_timer
    window.after_cancel(switch_timer)
    card = random.choice(card_words)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(display_word, text=card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    switch_timer = window.after(3000, func=switch_card)


#Switch to english
def switch_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(display_word, text=card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

#Delete card from list
def delete_card():
    card_words.remove(card) 
    data = pandas.DataFrame(card_words)
    data.to_csv("Day 31/data/words_to_learn.csv", index=False)
    get_word()



#Window
window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

switch_timer = window.after(3000, func=switch_card)

#images
incorrect = PhotoImage(file="Day 31/images/wrong.png")
correct = PhotoImage(file="Day 31/images/right.png")
card_back = PhotoImage(file="Day 31/images/card_back.png")
card_front = PhotoImage(file="Day 31/images/card_front.png")

#canvas
canvas = Canvas(width=830, height=650, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(420, 260, image=card_front)
language = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
display_word = canvas.create_text(400, 270, text="", font=("Ariel", 50, "bold"))
canvas.pack()

#buttons
correct_button = Button(image=correct, borderwidth=0, bg=BACKGROUND_COLOR, command=get_word)
correct_button.place(x=550, y=550,)

incorrect_button = Button(image=incorrect, borderwidth=0, bg=BACKGROUND_COLOR, command=delete_card)
incorrect_button.place(x=150, y=550,)

get_word()

window.mainloop()