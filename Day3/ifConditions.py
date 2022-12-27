# create a function that checks if the customer can get access to buy ticket or not. It should be at least 18 years old to get access.

age= int(input("Write your age \n"))
if age>=18:
    print("You can buy the ticket")
else:
    print("You are younger than 18. You can not buy a ticket from us.")