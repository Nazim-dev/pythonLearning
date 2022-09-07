#Calculate whether a year is a leap year
#On every year evenly divisible by 4
#except every year evenly divisible by 100
#unles the year is also evenly divisible by 400

year = int(input("What year do you want to check? "))

if year % 4 == 0:
    if year <= 100:
        print("Leap year")
    elif year % 400 == 0:
        print("Leap year")
    elif year % 100 == 0:
        print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")
