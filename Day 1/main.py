#Printing Text

print("This course is going to take a while," + 
"\nbut I need to do it to get where I want to be." +
"\nHopefully I can learn enough by november and" +
"\nearn enough to do at least one certification.")

#Taking input and printing

name = input("What's your name?")
info = "Your name has {} letters."
length = len(name)
print(info.format(length))

#Switch swap values in variables

a = input("a:")
b = input("b:")

c = b
b = a
a = c

print("a = " + a)
print("b = " + b)


#1. Create a greeting for your program
#2. Ask the user for the city that they live in.
#3. Ask the user for their pet's name.
#4. Combine both names to create their band name.

city = input("What city do you live in?\n")
petName = input("What's your pet's name?\n")
print("The name of your band is " + city + " " + petName)