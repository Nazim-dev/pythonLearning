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
game_images = [rock, paper, scissors]
compChoice = random.randint(0, 2)

print("you chose: ")
print(game_images[playerChoice])

print("Computer chose: ")
print(game_images[compChoice])

if playerChoice == compChoice:
    print("Tie")
elif playerChoice == 0 and compChoice == 2:
    print("You Win")
elif playerChoice > compChoice:
    print("You Win")
elif playerChoice < compChoice:
    print("You lose")
elif playerChoice == 2 and compChoice == 0:
    print("You lose")