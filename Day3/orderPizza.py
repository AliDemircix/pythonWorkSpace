
# Small pizza : $15
# Medium pizza: $20
# Large pizza: $25

# Pepperoni for small Pizza: $2
# Pepperoni for Medium or Large Pizza: $3

# Extra Cheese for any size : $1

print("Welcome to Python Pizza Delivery Service")

size = input("What size pizza do you want? S,M,L \n")
add_extra_cheese = input("Do you want extra cheese on your pizza? Y or N \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_s = 2
pepperoni_m_l = 3
extra_cheese = 1

total = 0

# if size == "S":
#     total = small_pizza
#     if add_extra_cheese == "Y":
#         total += extra_cheese
#     if add_pepperoni == "Y":
#         total += pepperoni_s
# elif size == "M":
#     total = medium_pizza
#     if add_extra_cheese == "Y":
#         total += extra_cheese
#     if add_pepperoni == "Y":
#         total += pepperoni_m_l
# elif size == "L":
#     total = large_pizza
#     if add_extra_cheese == "Y":
#         total += extra_cheese
#     if add_pepperoni == "Y":
#         total += pepperoni_m_l

if size == "S":
    total = small_pizza
elif size == "M":
    total = medium_pizza
elif size == "L":
    total = large_pizza
if add_extra_cheese == "Y":
    total += extra_cheese
if add_pepperoni == "Y":
    if size == "S":
        total += pepperoni_s
    else:
        total += pepperoni_m_l

print(
    f"Use ordered {size} pizza pepperoni {add_pepperoni} extra cheese {add_extra_cheese} total price is {total}")
