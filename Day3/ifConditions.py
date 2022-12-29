# create a function that checks if the customer can get access to buy ticket or not. It should be at least 18 years old to get access.

age = int(input("Write your age \n"))
if age >= 18:
    print("You can buy the ticket")
else:
    print("You are younger than 18. You can not buy a ticket from us.")

# Say if number odd or even

newNumber = int(input("Write a number"))

if newNumber % 2 == 0:
    print("Even")
else:
    print("Odd")

# Check height if >120cm  can write else cant write if can write check age>18 price $12 else price $7

customerHeight = int(input("Write your height \n"))

adultPrice = 12
childPrice = 7
if customerHeight >= 120:
    customerAge = int(input("Write your age \n"))
    if customerAge >= 18:
        print(f"Ticket price is {adultPrice}")
    else:
        print(f"Ticket price is {childPrice}")
else:
    print("You are not tall enough to ride.")
