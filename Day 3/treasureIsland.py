#Choose your own adventure game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to treasure island!")
print("your mission is to find treasure.")

choice = input("You're at a cross road. Do you want to go left or right? L OR R ")

if choice == "L":
    choice = input("You come to a lake. There is an island in the middle of the lake. Do you want to swim or wait? S OR W ")
    if choice == "W":
        choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Choose a door? R OR Y OR B ")
        if choice == "Y":
            print("You Win!")
        elif choice == "R":
            print("Burned by fire.")
            print("Game Over")
        elif choice == "B":
            print("Eaten by beasts")
            print("Game Over")
        else:
            print("Game Over")
    else:
        print("Attacked by trout")
        print("Game Over")
else:
    print("Fell into a hole")
    print("Game Over")