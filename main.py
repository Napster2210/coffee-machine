MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100}
COIN_VALUES = {"quarters": 0.25, "dimes": 0.1, "nickels": 0.05, "pennies": 0.01}
profit = 0


def check_resources(ingredients):
    """Returns True if the order can be made, False if ingredients are insufficient."""
    for item, amount in ingredients.items():
        if amount > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total amount of money calculated from inserted coins."""
    print("Please insert coins.")
    total = 0
    for coin, value in COIN_VALUES.items():
        try:
            total += int(input(f"How many {coin}?: ")) * value
        except ValueError:
            print(f"Invalid input for {coin}, treating as 0.")
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if the payment is accepted, False if money is insufficient."""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources and serves the coffee."""
    for item, amount in order_ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def print_report():
    """Prints the current status of the resources and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def coffee_machine():
    """Main loop for the coffee machine."""
    is_machine_on = True
    while is_machine_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            print("Turning off the machine!")
            is_machine_on = False
        elif user_choice == "report":
            print_report()
        elif user_choice in MENU:
            drink = MENU[user_choice]
            if check_resources(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(user_choice, drink["ingredients"])
        else:
            print("Invalid choice, please select from espresso, latte, or cappuccino.")


coffee_machine()
