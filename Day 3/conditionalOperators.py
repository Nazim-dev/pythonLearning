print("Welcom to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("Your ticket $5")
    elif age <= 18:
        print("Your ticket $7")
    else:
        print("Your ticket is $12")
else:
    print("You can't ride the roller coaster!")

