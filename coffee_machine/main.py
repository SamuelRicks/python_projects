"""
This program is designed to immulate a coffee machine

abstraction ideas...
coffee machine hold what? ingredients: water, milk, coffee.
coffee machine takes what? money: penny, nickel, dime, quater. request for type of coffe: expresso, latte, cappuccino

need to check amount of material to ensure accuracy...
need to check amount of money to ensure accuracy...

if there is not enough material to make a certain item... state that there is not enough
if the user did not supply enough money... state that there is insufficent funds.
"""

from data import MENU, resources

espresso = MENU["espresso"]
latte = MENU["latte"]
cappuccino = MENU["cappuccino"]
available_resources = resources


def intro():
    """
    ask the user for an item, then return a dictionary if item is correct
    """
    user_input = input("What item would you like to have: ESPRESSO, LATTE, CAPPUCCINO: ").lower()
    if user_input == "espresso":
        return espresso
    elif user_input == "latte":
        return latte
    elif user_input == "cappuccino":
        return cappuccino
    else:
        return

def compare_resources(coffee):
    """
    subtracts the coffee required ingredients from the resources available
    """
    global available_resources
    coffee_ingredients = coffee["ingredients"]
    for key in coffee_ingredients:
        if available_resources[key] >= coffee_ingredients[key]:
            available_resources[key] -= coffee_ingredients[key]
        else:
            print("insufficient resources")
            return False
    return True
    
def calculate_price():
    """
    returns the total price of the coins the user provided
    """
    pennies = int(input("number of pennies: ")) 
    nickels = int(input("number of nickels: ")) * 5
    dimes = int(input("number of dimes: ")) * 10
    quaters = int(input("number of quaters: ")) * 25
    total = (pennies + nickels + dimes + quaters) / 100
    return total

def compare_prices(coins_inserted, coffee_price):
    """
    compares the amount that is needed to purchase the product compared to what the user inputted
    """
    if coins_inserted == coffee_price:
        print("exact amount")
        return True
    elif coins_inserted > coffee_price:
        refund = coins_inserted - coffee_price
        print(f"Your refund is {refund}")
        return True
    else:
        print(f"Your balance is too low, full refund of {coins_inserted}")
        return False
    
def continue_program():
    user_input = input("Would you like to continue your request? y/n: ").lower()
    if user_input == "y":
        return False
    elif user_input == "n":
        return True
    else:
        return True

stop_request = False

def coffee_machine():
    global stop_request
    while not stop_request:
        selected_coffee = intro()
        if selected_coffee:
            if compare_resources(selected_coffee):
                coffee_price = selected_coffee["cost"]
                coins_inserted = calculate_price()
                compare_prices(coins_inserted, coffee_price)
        else:
            print("Invalid selection.")
        stop_request = continue_program()
        
        


coffee_machine()
