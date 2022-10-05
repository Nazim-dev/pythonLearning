from cgitb import text
from itertools import count
from tkinter import *
from tkinter.font import BOLD
import math

from numpy import imag
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            mark += "✔️"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer" ,fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="Day 28/tomato.png")
canvas.create_image(100, 113, image=tomato)
timer_text = canvas.create_text(101, 135, text="00:00", fill="white", font=(FONT_NAME, 30, BOLD))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()