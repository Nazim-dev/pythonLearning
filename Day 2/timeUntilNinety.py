#Create a program using maths and f-Strings that tells
#you how many days, weeks, months we have left if we live
#until 90 years old.Take the current
#age as input and output a message with our time left in
#this format "You have x days, y weeks and z months left"


import datetime

age = int(input("How old are you?"))

years_to_ninety = 90 - age

days_to_ninety = years_to_ninety * 365
weeks_to_ninety = years_to_ninety * 52
months_to_ninety = years_to_ninety * 12

print(f"You have {days_to_ninety} days, {weeks_to_ninety} weeks and {months_to_ninety} months left")