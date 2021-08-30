from data import MENU, resources

profit = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def check_money():
    print("Please enter a coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_resources(resources_needed):
    if water >= resources_needed["water"] and milk >= resources_needed["milk"] and coffee >= resources_needed["coffee"]:
        return True


def make_coffee(money, drink_resource, water, milk, coffee, cost):
    water -= drink_resource["water"]
    milk -= drink_resource["milk"]
    coffee -= drink_resource["coffee"]
    if money >= cost:
        refund = round(money - cost, 2)
        print(f"Here is ${refund} in change.")
        print("Here is your latte ☕️. Enjoy!")
    elif money < cost:
        print("Sorry that's not enough money. Money refunded.")

    return water, milk, coffee


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nprofit: ${profit}")
    else:
        drink_name = MENU[choice]
        drink_cost = drink_name["cost"]
        resources_has = check_resources(drink_name["ingredients"])
        if resources_has:
            profit += drink_cost
            money_received = check_money()
            resources_left = make_coffee(money_received, drink_name["ingredients"], water, milk, coffee, drink_cost)
            water -= resources_left[0]
            milk -= resources_left[1]
            coffee -= resources_left[2]
        else:
            print(f"Sorry, not enough resources available for drink {choice}.")
