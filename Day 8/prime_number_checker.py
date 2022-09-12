# prime number checker

def prime_checker(number):
    remain = 1
    for numbers in range(2, number):
        hold_num = number % numbers

        if hold_num < remain:
            remain = hold_num
            
    if remain == 0:
        print(f"{number} is not a prime number")

    else:
        print(f"{number} is a prime number")



n = int(input("Check this number: "))
prime_checker(number=n)
