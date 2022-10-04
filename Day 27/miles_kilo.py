from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=500, height=400)


#Labels

miles = Label(text="Miles", font=("Arial", 12))
miles.place(x=300, y=43)

equal = Label(text="is equal to", font=("Arial", 12))
equal.place(x=60, y=90)

ans = Label(text=" ", font=("Arial", 12))
ans.place(x=210, y=90)

kilo = Label(text="Km", font=("Arial", 12))
kilo.place(x=300, y=90)


#button

def button_clicked():
    mil = int(input.get())
    mil *=  1.609344
    ans["text"] = round(mil)

    


button = Button(text="Button",command=button_clicked)
button.place(x=200, y=130)


#entry

input = Entry(width=20)
input.place(x=160, y=50)

window.mainloop()
