print("Welcom to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Teen tickets are $7")
    elif age >= 45 and age <= 50:
        print("Seniors ride free")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("You can't ride the roller coaster!")

