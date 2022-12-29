# create a function that checks if the customer can get access to buy ticket or not. It should be at least 18 years old to get access.

# age = int(input("Write your age \n"))
# if age >= 18:
#     print("You can buy the ticket")
# else:
#     print("You are younger than 18. You can not buy a ticket from us.")

# Say if number odd or even

# newNumber = int(input("Write a number"))

# if newNumber % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Check height if >120cm  can write else cant write if can write check age>18 price $12 else price $7

customerHeight = int(input("Write your height \n"))

adultPrice = 10
childPrice = 5
photoPrice = 3
total = 0
if customerHeight >= 120:
    customerAge = int(input("Write your age \n"))
    if customerAge >= 18:
        total = adultPrice
    else:
        total = childPrice
    isPhotoWanted = input(
        "Do you want your trip photo with extra 3 euro cost ? \n Y or N \n")
    if isPhotoWanted == "Y":
        print(f"Total price is {total+photoPrice}")
    else:
        print(f"Total price is {total}")
else:
    print("You are not tall enough to ride.")
