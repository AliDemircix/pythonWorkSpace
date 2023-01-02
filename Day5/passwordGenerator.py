import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
           "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
specials = ["!", "@", "#", "$", "%", "^", "&", "*",
            "(", ")", "+", "-", ".", "`", "~", "|", "<", ">", "=", "-", "_"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

total = int(input("How many letters do you want in your password"))
total_special = int(
    input("How many special characters do you want in your password"))
total_number = int(input("How many numbers do you want in your password"))

password_list = []
password = ""

for x in range(1, total_special+1):
    password_list.append(random.choice(specials))
for x in range(1, total_number+1):
    password_list.append(random.choice(numbers))
for x in range(1, total-total_number-total_special+1):
    password_list.append(random.choice(letters))
random.shuffle(password_list) # random.shuffle changes order in an array
for char in password_list:
    password += str(char)
print(password)
