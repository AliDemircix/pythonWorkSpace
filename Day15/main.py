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
    if user_notification == "espresso":
        espresso_cost = MENU["espresso"]["cost"]
        refund = 0
        if check_resources(MENU['espresso']['ingredients']):
            if check_payment(money_payed, user_notification):
                refund = money_payed - espresso_cost
                print(f"Here is your {user_notification} and your refund {refund}")
                return refund
            else:
                print("Money is not enough")
        else:
            check_resources(MENU['espresso'])


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
        check_user_request(user_notification, totalMoney)
    askUser = input("Would you like to buy new one ? (y/n) ")
    if askUser == "y":

        askMoney = False
    else:
        close_machine = True

