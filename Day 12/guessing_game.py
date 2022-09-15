import random

print("Welcome to the Number Guessing Game!")


difficulty = input("Choose a difficulty, type 'easy' or 'hard' ")

print("Guess a number between 1 and 100 ")

def game(difficulty):

    hard = 5
    easy = 10

    rand_num = random.randrange(1, 100)

    if difficulty == "hard":
        while hard != 0:
            guess = int(input("Make a guess "))

            if rand_num < guess:
                print("Too High")
                hard -= 1
                print(f"{hard} tries remaining")
            elif rand_num > guess:
                print("Too Low")
                hard -= 1
                print(f"{hard} tries remaining")
            elif rand_num == guess:
                print(f"You got it, {guess} was the answer")

    if difficulty == "easy":
        while easy != 0:
            guess = int(input("Make a guess "))

            if rand_num < guess:
                print("Too High")
                easy -= 1
                print(f"{easy} tries remaining")
            elif rand_num > guess:
                print("Too Low")
                easy -= 1
                print(f"{easy} tries remaining")
            elif rand_num == guess:
                print(f"You got it, {guess} was the answer")


game(difficulty)