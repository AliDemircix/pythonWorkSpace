# https://www.askpython.com/ use to learn something

import random
import my_module  # custom module that we created

# print(random_integer,my_module.pi)

random_integer = random.randint(1, 2)
random_float = random.random()*5  # not included 5 0.0-4.9999999

if random_integer == 1:
    print("Heads")
else:
    print("Tails")
