#Write a program that calculates the Body Mass Index from a user's
#weight and height.
#The BMI is calculated by dividing a person's weight(in kg)
#by the square of thier heigh (in m)

weight = float(input ("enter weight in kg: "))
height = float(input ("enter height in m: "))

bmi = weight / (height*height)

print("Your BMI is " + str(bmi))