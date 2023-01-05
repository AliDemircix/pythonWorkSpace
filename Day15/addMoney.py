from constants import twentyfive_cent, fifty_cent, two_euro, one_euro


def add_money():
    amount_of_twentyfive = float(input("Add twentyfive coin:"))
    amount_of_fifty = float(input("Add fifty coin:"))
    amount_of_one_euro = float(input("Add 1 euro coin:"))
    amount_of_two_euro = float(input("Add 2 euro coin:"))
    total = amount_of_twentyfive * twentyfive_cent + amount_of_fifty * fifty_cent + amount_of_two_euro * two_euro \
            + amount_of_one_euro * one_euro
    return total
