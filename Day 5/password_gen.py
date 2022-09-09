#passord generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
if nr_letters < 1:
    print("Invalid input \n")

nr_symbols = int(input(f"How many symbols would you like?\n"))
if nr_symbols < 1:
    print("Invalid input \n")

nr_numbers = int(input(f"How many numbers would you like?\n"))
if nr_numbers < 1:
    print("Invalid input \n")


password = []

for letter in range(0, nr_letters):
    rand = random.randint(0, 51)
    password += letters[rand]

for number in range(0, nr_numbers):
    rand = random.randint(0, 9)
    password += numbers[rand]

for symbol in range(0, nr_symbols):
    rand = random.randint(0, 8)
    password += symbols[rand]

random.shuffle(password)

print(''.join(password))
