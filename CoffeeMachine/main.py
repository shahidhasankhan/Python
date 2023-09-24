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
    "money": 0.0
}


def print_report():
    print(f"Water  : {resources['water']}mL")
    print(f"Mill   : {resources['milk']}mL")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money  : ${resources['money']}")


def check_ingredients(coffee_type):
    coffee_recipe = MENU[coffee_type]["ingredients"]
    for ingredient in coffee_recipe:
        if resources[ingredient] < coffee_recipe[ingredient]:
            print(f"Sorry! Not enough {ingredient}")
            return False
    return True


def get_money(coffee_type):
    quarters = int(input("Insert Quarters: "))
    dimes = int(input("Insert Dimes: "))
    nickles = int(input("Insert Nickles: "))
    pennies = int(input("Insert Pennies: "))
    money_inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    cost_of_coffee = MENU[coffee_type]["cost"]
    if money_inserted < cost_of_coffee:
        print(f"{coffee_type} costs {cost_of_coffee}! Please take your ${money_inserted} back")
        return False
    else:
        resources["money"] += cost_of_coffee
        change = money_inserted - cost_of_coffee
        if change > 0:
            print(f"Here's your change : ${change}")
        return True


def make_coffee(coffee_type):
    coffee_recipe = MENU[coffee_type]["ingredients"]
    for ingredient in coffee_recipe:
        resources[ingredient] -= coffee_recipe[ingredient]
    print(f"Here's your {coffee_type}. Please enjoy!")


def use_coffee_machine():
    while 1:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            return
        elif user_choice == "report":
            print_report()
        else:
            if check_ingredients(user_choice) and get_money(user_choice):
                make_coffee(user_choice)


use_coffee_machine()
