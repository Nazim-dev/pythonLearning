import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = "y"

#Checks if player or computer has 21 on first draw. If they do then it's an automatic win "BlackJack"
def black_jack(user_cards, comp_cards):
    sum1 = 0
    sum2 = 0
    
    for card in comp_cards:
        sum2 += card
        if sum2 == 21:
            print(f"BlackJack {sum2} \nComp win!")
            return True
    
    for card in user_cards:
        sum1 += card
        if sum1 == 21:
            print(f"BlackJack {sum1} \nYou win!")
            return True
    return False

#Compares hand totals to generate a result
def compare(total, total2):

    if total > 21:
        print(f"Hand {total} and Comp {total2} \nYou Lose!")
    elif total2 > 21:
        print(f"Your hand {total} and Comp {total2} \nYou Win!")
    elif total > total2 and total < 21:
        print(f"Your hand {total} and comp hand {total2}. You Win! ")
    elif total2 > total and total2 < 21:
        print(f"Your hand {total} and comp hand {total2}. You Lose! ")
    elif total == total2:
        print(f"Your hand {total} and comp hand {total2}. Draw! ")
    else:
        print(f"Your hand {total} and comp hand {total2}. You Lose! ")

#Adds up all cards in hand
def sum_cards(hand):   
    amount = 0
    for i in hand:
        amount += i
    
    for i in hand:
        if i == 11 and amount > 21:
            hand.remove(11)
            hand.append(1)
    return amount


while game == "y":
    os.system('cls')
    user_cards = []
    comp_cards = []
    skip = False
    choice = "y"

    for i in range(2):
        user_cards.append(random.choice(cards))
        
    for i in range(2):
        comp_cards.append(random.choice(cards))
    
    total = sum_cards(user_cards)
    total2 = sum_cards(comp_cards)

    print(f"Here are your cards {user_cards}, total = {total}")
    print(f"Dealer's first card {comp_cards[0]} \n")

    skip = black_jack(user_cards, comp_cards)

    #skips other part of the game if a win is achieved with the first draw
    if skip == False:
        while choice == "y":
            choice = input("Do you want to draw another card? y or n  ")
            if choice == "y":
                user_cards.append(random.choice(cards))
                total = sum_cards(user_cards)
                print(f"Here are your cards {user_cards}, total = {total}")

    #Forces the computer to keep drawing cards if it's hand is too low
    while total2 < 16:
        comp_cards.append(random.choice(cards))
        total2 = sum_cards(comp_cards)
                
    compare(total, total2)
    game = input("Play again? y or n ")