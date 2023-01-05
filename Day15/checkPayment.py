from constants import MENU


def check_payment(total_money, user_notification):
    return float(total_money) >= float(MENU[user_notification]["cost"])
