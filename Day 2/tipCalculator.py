#Calculate the tip need to be paid by each person/s

print("welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
rate = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill?  "))

if rate == 10 or rate == 12 or rate == 15:
    total_tip = bill * (rate / 100)
    total = (bill + total_tip) / people
    total = round(total, 2)
    print(f"Each person should pay: ${total}")
else:
    print("You entered an incorrect percentage, please try again")

