from email import message
from tkinter import *
from tkinter import messagebox
import random
import json
from numpy import pad

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_input.insert(0, password)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = web_input.get()
    try:
        with open("Day 29/Account_info.json", "r") as file:
            data = json.load(file)
    
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File doesn't exist")
    
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="Website doesn't exist in File")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    email = email_input.get()
    website = web_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Try again", message="Please fill all fields")
    else:
        try:
            with open("Day 29/Account_info.json", "r") as file:
                data = json.load(file)
                data.update(new_data)

        except FileNotFoundError:
            with open("Day 29/Account_info.json", "w") as file:
                json.dump(new_data, file, indent= 4)
                
        else:
            with open("Day 29/Account_info.json", "w") as file:
                json.dump(data, file, indent= 4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="Day 29/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website: ", font=("Arial", 12))
website.grid(column=0, row=1)

web_input = Entry(width=18)
web_input.grid(column=1 , row=1)
web_input.focus()

search = Button(text="Search", width=15, command=find_password)
search.grid(column=2, row=1)


email = Label(text="Email/Username: ", font=("Arial", 12))
email.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1 , row=2, columnspan=2)
email_input.insert(0, "bob@outlook.com")

password = Label(text="Password: ", font=("Arial", 12))
password.grid(column=0, row=3)

pass_input = Entry(width=18)
pass_input.grid(column=1 , row=3)

generate_pass = Button(text="Generate Password", command=create_password)
generate_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_info)
add_button.grid(column=1, row=4, columnspan=3)

window.mainloop()