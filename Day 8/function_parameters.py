#simple function

def greet():
    print("Hello")
    print("Hope you're doing well!")
    print("Have a great night")

greet()

#Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Fred")

#Functions with multiple inputs and keywords

def greet_with(name , location):
    print(f"How are you doing {name}")
    print(f"Are you enjoying {location}")

greet_with(location = "Grenada", name = "Nazim")