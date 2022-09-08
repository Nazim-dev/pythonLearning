#Sum the occurences of the letter in "True Love" occur in
#the names of both people

print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

digit1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
digit1 = digit1 + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

digit2 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
digit2 = digit2 + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

sum = int(f"{digit1}{digit2}")

if sum < 10 or sum > 90:
    print(f"Your score is {sum}, you go together like coke and mentos")
elif sum >= 40 and sum <= 50:
    print(f"Your score is {sum}, you are alright together")
else:
    print(f"Your score is {sum}")


