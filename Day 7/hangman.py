
import random
import hangman_art
import hangman_words
import os

print(hangman_art.logo)

lives = 6
word_list = hangman_words.word_list
choosen_word = random.choice(word_list)
letter_hold = ""

display = []
for letter in choosen_word:
    display.append("_")

print(display)

while "_" in display and lives != 0:
    guess = input("Guess a letter \n").lower()
    
    os.system("cls")

    if guess in display:
        print(f"You already tired letter {guess}")
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        
        if guess == letter:
            display[position] = guess
            letter_hold = guess
    
    if lives > -1 and guess != letter_hold:
        lives -= 1
        print(hangman_art.stages[lives])
        print(f"The letter {guess} is not in the word, {lives} tries left ")
    
    print(display)

    if lives == 0:
        print("You lose")

if "_" not in display:
    print("You Win")


