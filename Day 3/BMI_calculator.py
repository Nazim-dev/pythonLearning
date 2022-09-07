#Write a program that calculates the Body Mass Index from a user's
#weight and height.
#The BMI is calculated by dividing a person's weight(in kg)
#by the square of thier heigh (in m)

weight = float(input ("enter weight in kg: "))
height = float(input ("enter height in m: "))

bmi = round(weight / (height*height),1)

print("Your BMI is " + str(bmi))

if bmi < 18.5:
    print("You are under weight")
elif bmi < 25:
    print ("Your weight is normal")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")