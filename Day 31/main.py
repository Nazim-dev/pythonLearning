from cProfile import label
from random import randint
from tkinter import *
import pandas
from setuptools import Command

BACKGROUND_COLOR = "#B1DDC6"
LABEL_COLOR = "#FFFFFF"
CARD_COLOR = "#91C2AF"
FRENCH_COLOR = "#000000"
english = None
french = None
card_words = None

#Switch to english
def switch_card():
    canvas.itemconfig(canvas_image, image=card_back)
    language.config(text="English", fg=LABEL_COLOR, bg=CARD_COLOR)
    word.config(text=english, fg=LABEL_COLOR, bg=CARD_COLOR)

#Delete word
def delete_word():

    for i in list(card_words["French"]):
            if i == french:
                del card_words["French"][i]

    for i in list(card_words["English"]):
        if i == english:
            del card_words["English"][i]

    cards_df = pandas.DataFrame(card_words)
    cards_df.to_csv("Day 31/data/words_to_learn.csv")

#Get csv
def get_word():
    global english
    global french

#use list instead of dictionary
    with open("Day 31/data/french_words.csv") as file:
        data = pandas.read_csv(file)
        card_words = data.to_dict()
        select = randint(0,101)
        french = card_words["French"][select]
        english = card_words["English"][select]

        canvas.itemconfig(canvas_image, image=card_front)
        language.config(text="French", bg=LABEL_COLOR, fg=FRENCH_COLOR)
        word.config(text=french, bg=LABEL_COLOR, fg=FRENCH_COLOR)

        window.after(3000, switch_card)



#Window
window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

#images
incorrect = PhotoImage(file="Day 31/images/wrong.png")
correct = PhotoImage(file="Day 31/images/right.png")
card_back = PhotoImage(file="Day 31/images/card_back.png")
card_front = PhotoImage(file="Day 31/images/card_front.png")

#canvases
canvas = Canvas(width=830, height=650, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(420, 260, image=card_front)
canvas.pack()

#Labels
language = Label(text="French", bg=LABEL_COLOR, font=("Ariel", 30, "italic"))
language.place(x=325, y=75)

word = Label(text="Ready?", bg=LABEL_COLOR, font=("Ariel", 50, "bold"))
word.place(x=265, y=200)

#buttons
correct_button = Button(image=correct, borderwidth=0, bg=BACKGROUND_COLOR, command=get_word)
correct_button.place(x=550, y=550,)

incorrect_button = Button(image=incorrect, borderwidth=0, bg=BACKGROUND_COLOR, command=get_word)
incorrect_button.place(x=150, y=550,)

window.mainloop()