from data import MENU, resources, money


def check_resources():
    """Checks resources sufficiency """
    proceed = True
    for x in choice_ingredient:
        if choice_ingredient[f'{x}'] > resources[f'{x}']:
            print(f"Sorry there is not enough {x}")
            proceed = False

    return proceed


def monetary_value(quatz, dime, nicks, penn):
    """Calculates the coins"""
    total = round(float((0.23 * quatz) + (0.10 * dime) + (0.05 * nicks) + (0.01 * penn)), 2)
    return total


def check_transaction():
    """Checks if the cash is enough to buy a coffee"""
    proceed = True
    if user_cash >= choice_cost:
        if user_cash > choice_cost:
            change = round(user_cash - choice_cost, 2)
            print(f"Here is ${change} in change")
            user_payment = choice_cost
            return proceed, user_payment
        else:
            user_payment = user_cash
            return proceed, user_payment
    else:
        print(f"{user_drink} cost {choice_cost} and your money is {user_cash}."
              f"\nSorry that's not enough money, Money refunded")
        proceed = False
        user_payment = 0
        return proceed, user_payment


machine_on = True
while machine_on:
    available_water = resources['water']
    available_milk = resources['milk']
    available_coffee = resources['coffee']
    available_money = money['profit']

    user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    choice = False
    choice_ingredient = {}
    choice_cost = 0

# Checks if input is in the dictionary and selects ingredients and cost
    for i in MENU:
        if user_drink == i:
            choice_ingredient = MENU[f'{i}']['ingredients']
            choice_cost = MENU[f'{i}']['cost']
            choice = True

    if choice:
        if check_resources():
            # collects the coins
            print("Please insert coin")
            quarters = int(input("how many quarters: "))
            dimes = int(input("how many dimes: "))
            nickles = int(input("how many nickles: "))
            pennies = int(input("how many pennies: "))

            user_cash = monetary_value(quarters, dimes, nickles, pennies)

            proceed_value, payment_value = check_transaction()

            if proceed_value:
                # Deducts used resources from the resources
                for item in choice_ingredient:
                    resources[f'{item}'] -= choice_ingredient[f'{item}']

                money["profit"] += payment_value
                print(f"Here is your {user_drink}, Enjoy!")

    elif user_drink == 'report':
        print(f"water: {available_water}ml\nMilk: {available_milk}ml\nCoffee: {available_coffee}ml\n"
              f"Money: ${available_money}")

    elif user_drink == 'end':
        machine_on = False

    else:
        print("Invalid input")
