#program to choose random names and select who pays the bill

import random

print("Welcome to banker Roulette!")
print("Please space out the names!")

friend_group = []
friend_group = input("Enter everyone's name ").split()


group_size = len(friend_group)

person = random.randint(0, group_size) -1
print(person)

print(f"{friend_group[person]} is going to buy the meal today!")