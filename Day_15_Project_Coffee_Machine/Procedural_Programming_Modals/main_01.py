MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

resources = {"water": 300, "milk": 200, "coffee": 100}
money = 0.0


def check_resource(choice):
    ingredients = MENU[choice]["ingredients"]

    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            return f"Sorry, not enough {item} to make {choice}."

    return "sufficient"


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return round(quarters + dimes + nickels + pennies, 2)


def make_coffee(choice):
    ingredients = MENU[choice]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]


def coffee_machine():
    global money
    is_on = True

    while is_on:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        if choice == 'off':
            print("Turning off the coffee machine. Goodbye!")
            is_on = False
            break

        elif choice == 'report':
            print(f"\nWater: {resources['water']}ml")
            print(f"Milk: {resources.get('milk', 0)}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"💰 Money: ${money:.2f}\n")
            continue

        elif choice in MENU:
            message = check_resource(choice)
            if message != "sufficient":
                print(message)
                continue

            cost = MENU[choice]["cost"]
            payment = process_coins()

            if payment < cost:
                print("Sorry, that's not enough money. Money refunded.")
                continue
            else:
                if payment > cost:
                    change = round(payment - cost, 2)
                    print(f"Here is ${change} in change.")
                money += cost
                make_coffee(choice)
                print(f"☕ Here is your {choice}. Enjoy!")

        else:
            print("Invalid input. Please enter espresso, latte, cappuccino, report, or off.")


coffee_machine()
