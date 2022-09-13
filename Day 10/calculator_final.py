import calculator_art

#Calulator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return round(n1 + n2, 2)


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for sign in operations:
    print(sign)
operation_symbol = input("Pick an operation from the line above: ")
calculation = operations[operation_symbol]
answer = calculation(num1, num2)
    

print(f"{num1} {operation_symbol} {num2} = {answer}")