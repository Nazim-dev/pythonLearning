from game_data import data
from art import logo, vs
import random

counter = 0
score = 0

print(logo)

"""Pulls people from the list"""

def get_persons(score):
    person1 = random.choice(data)
    person2 = random.choice(data)
    
    """The 'IF' ets 2 random people and the 'ELSE' gets 1 random person"""
    if score == 0:
        print("Who has more Instagram followers?")
        print("Compare A: ", person1["name"], person1["description"], "from" , person1["country"])
        print(vs)
        print("Against B: ", person2["name"], person2["description"], "from" , person2["country"])
        return person1, person2
    else:
        
        person2 = random.choice(data)
        print("Who has more Instagram followers?")
        print("Compare A: ", person3["name"], person3["description"], "from" , person3["country"])
        print(vs)
        print("Against B: ", person2["name"], person2["description"], "from" , person2["country"])
        return person3, person2
        
    

"""Compare the followers of the two people pulled from the list and returns the answer"""
def compare(persons):
    #Second person needs to be used again in "get_person" function so it's stored in a global variable
    global person3
    person1 = persons[0]
    person2 = persons[1]
    person3 = person2 

    followers1 = person1["follower_count"]
    followers2 = person2["follower_count"]

    if followers1 > followers2:
        return "A" 
    else:
        return "B"

"""Check answer against user input"""
def choose(ans):
    choice = input("Type 'A' or 'B': ")
    
    if choice == ans[0]:
        return 1
    else:
        print(f"You lose")
        return 0

while counter != -1 :
    answer = compare(get_persons(score))
    counter = choose(answer)

    if counter == 0:
        counter = -1
    else:
        score += counter

print(f"Your score is {score}")

