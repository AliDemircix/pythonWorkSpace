from constants import MENU


def check_payment(total_money, user_notification):
    return total_money >= MENU[user_notification]["cost"]
