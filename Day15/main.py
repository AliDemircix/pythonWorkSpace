from showResources import show_resources
from constants import MENU, resources
from addMoney import add_money
from checkPayment import check_payment
from checkResources import check_resources


def ask_customer_prefer():
    return input("What would you like? (espresso/latte/cappuccino)")


def check_user_request(user_notification, money_payed):
    if user_notification == "report":
        show_resources(resources)
    if user_notification != "report":
        coffee_cost = MENU[user_notification]["cost"]
        refund = 0
        if check_resources(MENU[user_notification]['ingredients']):
            if check_payment(money_payed, user_notification):
                refund = money_payed - coffee_cost
                print(f"Here is your {user_notification} and your refund {refund}")
                return refund
            else:
                print("Money is not enough")
        else:
            print("Resources is not enough for new coffee ")


close_machine = False
askMoney = True
totalMoney = 0
user_notification = ask_customer_prefer()
while not close_machine:

    if askMoney:
        money_paid = add_money()
        totalMoney = check_user_request(user_notification, money_paid)
    else:
        user_notification = ask_customer_prefer()
        totalMoney = check_user_request(user_notification, totalMoney)
    askUser = input("Would you like to buy new one ? (y/n) ")
    if askUser == "y":

        askMoney = False
    else:
        close_machine = True

