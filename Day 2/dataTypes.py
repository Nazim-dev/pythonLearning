print(123_3456_789)
print(70 + float("100.5"))
print(str(20) + str(342))

#Write a program that adds digits in a 2 digit number
#e.g. If you input 24, the output should be 6 (2+4=6)

two_digit_number = input("Type a two digit number: ")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

sum = first_digit + second_digit

print(sum)

print(round(8/3, 2))
print(8//3)