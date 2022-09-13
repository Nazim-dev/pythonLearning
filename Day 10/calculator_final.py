import calculator_art

print(calculator_art.logo)

# Calulator

# Add


def add(n1, n2):
    return round(n1 + n2, 2)

# Subtract


def subtract(n1, n2):
    return round(n1 - n2, 2)

# Multiply


def multiply(n1, n2):
    return round(n1 * n2, 2)

# Divide


def divide(n1, n2):
    return round(n1 / n2, 2)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    num1 = float(input("What's the first number?: "))

    choice = "y"
    while choice == "y":
        num2 = float(input("What's the next number?: "))
        for sign in operations:
            print(sign)
        operation_symbol = input("Pick an operation from the line above: ")
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start new calculator or 'e' to exit: ")
        if choice == 'y':
            num1 = answer
        elif choice == 'n' :
            calculator()

calculator()
