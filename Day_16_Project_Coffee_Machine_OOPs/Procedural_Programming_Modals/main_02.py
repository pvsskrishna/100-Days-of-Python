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
profit = 0.0

def check_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("please insert the coins")
    total = int(input(f"How many Quarters?: ")) * 0.25
    total+= int(input(f"How many Dimes?: ")) * 0.1
    total+= int(input(f"How many Nickles?: ")) * 0.05
    total+= int(input(f"How many Pennies?: ")) * 0.01
    return total

def check_transaction_successful(received_money,drink_cost):
    if received_money > drink_cost:
        balance = round(received_money-drink_cost,2)
        print(f"Here is ${balance} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!☕")

def coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino):")

        if choice == 'off':
            print("Coffee machine is getting shut down!")
            is_on = False
        elif choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[choice]
            if check_resources_sufficient(drink['ingredients']):
                payment = process_coins()
                if check_transaction_successful(payment, drink['cost']):
                    make_coffee(choice,drink['ingredients'])

coffee_machine()




