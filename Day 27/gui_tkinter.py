import tkinter 

window = tkinter.Tk()
window.title("First time")
window.minsize(width=500, height=400)


#Label

the_label = tkinter.Label(text="Label here", font=("Arial", 24))
the_label.pack()



window.mainloop()
