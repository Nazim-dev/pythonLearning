from machine_data import menu, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
espresso = menu["espresso"]
latte = menu["latte"]
cappuccino = menu["cappuccino"]
money_made = 0.0
order_no = 1
choice = "y"


def order_coffee(drink):
    if drink == "latte":
        ingredients = latte["ingredients"]
    elif drink == "espresso":
        ingredients = espresso["ingredients"]
    elif drink == "cappuccino":
        ingredients = cappuccino["ingredients"]
    else:
        print("Please enter a drink on the list")
        return

    return drink, ingredients

def check_resources(drink_ingredients, water, coffee, milk, order_no):

    drink = drink_ingredients[0]
    ingredients = drink_ingredients[1]

    if order_no > 1:
        if ingredients["water"] > water:
            print("Insufficent water")
            return False
        elif drink != "espresso" and ingredients["milk"] > milk:
            print("Insufficent milk")
            return False
        elif ingredients["coffee"] > coffee:
            print("Insufficent coffee")
            return False

    return True
    
def new_resources(drink_ingredients, water, coffee, milk):
    drink = drink_ingredients[0]
    ingredients = drink_ingredients[1]

    if drink != "espresso":
        water -= int(ingredients["water"])
        milk -= int(ingredients["milk"])
        coffee -= int(ingredients["coffee"])
        return [water, coffee, milk]
    else:
        water -= int(ingredients["water"])
        coffee -= int(ingredients["coffee"])
        return [water, coffee, milk]

def pay(drink):
    paid = 0.0
    latte_price = latte["cost"]
    espresso_price = espresso["cost"]
    cappuccino_price = cappuccino["cost"]
    quarters = int(input("How many quarters? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))

    paid += (quarters * 0.25) + (nickles * 0.1) + (pennies * 0.01)

    if drink == "latte" and paid > latte_price:
        print(f"Here's your {drink}. Enjoy!")
        print(f"Your change is ${round(paid - latte_price, 2)}.")
        return latte_price 
    elif drink == "espresso" and paid > espresso_price:
        print(f"Here's your {drink}. Enjoy!")
        print(f"Your change is ${round(paid - espresso_price, 2)}.")
        return espresso_price
    elif drink == "cappuccino" and paid > cappuccino_price:
        print(f"Here's your {drink}. Enjoy!")
        print(f"Your change is ${round(paid - cappuccino_price, 2)}.")
        return cappuccino_price
    
    print(f"Not enough money, here's your refund ${paid}")
    return 0

def report(water, coffee, milk, money_made):
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money_made}")

while choice == "y":
    order = input("What would you like? (espresso/latte/cappuccino): \n")
    
    if order == "report":
        report(water, coffee, milk, money_made)
        order = input("What would you like? (espresso/latte/cappuccino): \n")

    elif order == "off":
        break

    drink_ingredients = order_coffee(order)

    if check_resources(drink_ingredients, water, coffee, milk, order_no) == True:
        water_coffee_milk = new_resources(drink_ingredients, water, coffee, milk)
        water = water_coffee_milk[0]
        coffee = water_coffee_milk[1]
        milk = water_coffee_milk[2]
        money_made += pay(order)
        order_no += 1
        choice = input("Would you like to order again? y or n ")
    else:
        print("Sorry for the inconvenience")
        choice = "n"

