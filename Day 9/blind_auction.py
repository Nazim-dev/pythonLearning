import os
import auction_logo

print(auction_logo.logo)
ans = "yes"
bidding = {}
highest = 0
def place_bid(name, amount):
    bidding[name] = amount
        

            
while ans == "yes":
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    ans = input("Are there any other bidders? 'yes or 'no' ")
    os.system("cls")
    place_bid(name,bid)
    
for bidder in bidding:
    if bidding[bidder] > highest:
        highest = bidding[bidder]
        winner = bidder
        

print(f"The winner {winner} is with a bid of ${highest}")
