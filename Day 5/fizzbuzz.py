#print each number from 1 to 100 in turn.
#when the number is divisible by 3 then instead of printing the number, it should print "Fizz"
#when the number is divisible by 5 then instead of printing the number, it should print "Buzz"
#when the number is divisible by both 3 and 5 , it should print "FizzBuzz"

for numbers in range(1,100):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 5 == 0:
        print("Buzz")
    elif numbers % 3 == 0:
        print("Fizz")
    else:
        print(numbers)
