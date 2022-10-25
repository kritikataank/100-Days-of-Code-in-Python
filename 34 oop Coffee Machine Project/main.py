from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


go_on = True

while go_on:
    options = menu.get_items()
    want = input(f"What would you like? ({options}): ")
    if want == "off":
        go_on = False
    elif want == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(want)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)