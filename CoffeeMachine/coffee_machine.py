import main
import math
from main import MENU
def turn_off_machine(maintainer_code):
    return maintainer_code == "off"


def print_report(resources ):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def is_resources_sufficient(resources, current_order):
    if resources['water'] < MENU[current_order]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False
    elif current_order != "espresso" and resources['milk'] < MENU[current_order]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
        return False
    elif resources['coffee'] < MENU[current_order]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    return True


def get_coins_from_the_customer():
    coins = {}
    print("Please insert coins.")
    coins['quarters'] = float(input("how many quarters?: "))
    coins['dimes'] = float(input("how many dimes?: "))
    coins['nickles'] = float(input("how many nickles?: "))
    coins['pennies'] = float(input("how many pennies?: "))
    return coins


def convert_to_dollars(coins):
    coins_in_dollars = {}
    coins_in_dollars['quarters'] = coins['quarters'] * 0.25
    coins_in_dollars['dimes'] = coins['dimes'] * 0.10
    coins_in_dollars['nickles'] = coins['nickles'] * 0.05
    coins_in_dollars['pennies'] = coins['pennies'] * 0.01
    return coins_in_dollars

def paid_total(dollars):
    sum = 0
    for dollar in dollars:
        sum += dollars[dollar]
    return sum


def process_coins(coins):
    return convert_to_dollars(coins)

def is_enough_money_paid(money_paid, coffee_drinks, customer_drink_type):
    drink_cost = coffee_drinks[customer_drink_type]['cost']
    return money_paid >= drink_cost

def return_change(money_paid, coffee_drinks, customer_drink_type):
    drink_cost = coffee_drinks[customer_drink_type]['cost']
    return round(money_paid - drink_cost, 2)

def dispense_drink(resources, drink_cost, drink_type):
    print(f"Here is your {drink_type} ☕️. Enjoy!")
    return resources['money'] + drink_cost


def update_resources(resources, drink_type):
    resources['water'] -= MENU[drink_type]['ingredients']['water']
    if drink_type != "espresso":
        resources['milk'] -= MENU[drink_type]['ingredients']['milk']
    resources['coffee'] -= MENU[drink_type]['ingredients']['coffee']
    resources['money'] += MENU[drink_type]['cost']
    return resources


def coffee_machine():
    is_machine_on = True
    resources = main.resources
    resources['money'] = 0
    while is_machine_on:
        user_option = input("What would you like? (espresso/latte/cappuccino): ")
        if user_option == "off":
            is_machine_on = False
        elif user_option == "report":
            print_report(resources)
        else:
            if is_resources_sufficient(resources, user_option):
                coins = get_coins_from_the_customer()
                dollars = process_coins(coins)
                total_amount_paid = paid_total(dollars)
                if is_enough_money_paid(total_amount_paid, MENU, user_option):
                    change =  return_change(total_amount_paid, MENU, user_option)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    dispense_drink(resources, MENU[user_option]['cost'], user_option)
                    resources = update_resources(resources, user_option)
                else:
                    print("Sorry that's not enough money. Money refunded.")

coffee_machine()






#Here is $8.43 in change.
