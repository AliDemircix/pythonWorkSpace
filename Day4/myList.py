import random
states_of_netherlands = ["Leiden", "Amsterdam",
                         "Wassenaar", "Den Haag", "Rotterdam"]
states_of_netherlands[2] = "Updated State"
states_of_netherlands.append("Last added state")
# print(states_of_netherlands[-1])


# Create an input gets  name then conver them list and select one of them randomly and print to lucky person

customers = input("Type customer list names with comma.\n")
customer_list = customers.split(", ")
print(customer_list)
# lucky_one= customer_list[random.randint(0,len(customer_list)-1)]
lucky_one = random.choice(customer_list) # if you want to choise one of them dont need to make random list just use choice
print(f"Todays lucky person is {lucky_one}")
