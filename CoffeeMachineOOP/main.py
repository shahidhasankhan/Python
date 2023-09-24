from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

is_machine_on = True

while is_machine_on:
    user_choice = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        user_order = coffee_menu.find_drink(user_choice)
        if my_coffee_maker.is_resource_sufficient(user_order):
            if my_money_machine.make_payment(user_order.cost):
                my_coffee_maker.make_coffee(user_order)
