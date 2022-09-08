#rock paper scissors game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcom to Rock, Paper, Scissors!")

playerChoice = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors "))

compChoice = random.randint(0, 2)

if playerChoice == 0 and compChoice == 0:
    print(rock)
    print("Computer chose: ")
    print(rock)
    print("Tie")
elif playerChoice == 0 and compChoice == 1:
    print(rock)
    print("Computer chose: ")
    print(paper)
    print("You lose")
elif playerChoice == 0 and compChoice == 2:
    print(rock)
    print("Computer chose: ")
    print(scissors)
    print("You Win")

elif playerChoice == 1 and compChoice == 1:
    print(paper)
    print("Computer chose: ")
    print(paper)
    print("Tie")
elif playerChoice == 1 and compChoice == 2:
    print(paper)
    print("Computer chose: ")
    print(scissors)
    print("You lose")
elif playerChoice == 1 and compChoice == 0:
    print(paper)
    print("Computer chose: ")
    print(rock)
    print("You Win")

elif playerChoice == 2 and compChoice == 2:
    print(scissors)
    print("Computer chose: ")
    print(scissors)
    print("Tie")
elif playerChoice == 2 and compChoice == 0:
    print(scissors)
    print("Computer chose: ")
    print(rock)
    print("You lose")
elif playerChoice == 2 and compChoice == 1:
    print(scissors)
    print("Computer chose: ")
    print(paper)
    print("You Win")