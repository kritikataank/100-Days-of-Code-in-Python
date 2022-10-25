MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sufficient_resource(order_ingredients):
    """Returns True when order can be made, False when ingredients are insufficient"""
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, False if money is insufficient. """
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} change.")
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name}")


go_on = True
profit = 0

while go_on:
    want = input("What would you like? (expresso/latte/cappuccino): ")
    if want == "off":
        go_on = False
    elif want == "report":
        print(f"water = {resources['water']}ml")
        print(f"milk = {resources['milk']}ml")
        print(f"coffee = {resources['coffee']}g")
        print(f"Money = ${profit}")
    else:
        drink = MENU[want]
        if sufficient_resource(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(want, drink["ingredients"])