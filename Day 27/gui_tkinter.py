from tkinter import *

window = Tk()
window.title("First time")
window.minsize(width=500, height=400)


#Label

the_label = Label(text="Label here", font=("Arial", 18))
the_label.grid(column=0, row=0)

#button

def button_clicked():
    text = input.get()
    the_label["text"] = text
    


button = Button(text="Button",command=button_clicked)
button.grid(column=2, row=2)


#entry

input = Entry(width=20)
input.grid(column=1, row=1)

window.mainloop()
