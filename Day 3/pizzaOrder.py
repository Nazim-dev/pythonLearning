#based on the users order, calculate their bill
#small pizza 15, medium 20, large 25
#pepperoni for small +2, pepperoni for medium or large +3
#extra cheese any size +1

print("welcome to the pizzaria!")
size = input("What size pizza do you want? S, M, L ")
pepperoni = input("Do you want pepperoni? Y OR N ")
extra_cheese = input("Do you want extra cheese? Y OR N ")

bill = 0

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
            bill += 1
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
            bill += 1
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
            bill += 1

print(f"Your final bill is: ${bill}")


        