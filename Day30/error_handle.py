# # FileNotFound

# try:
#     file = open("Day30/a_file.txt")  # This will try to open
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:  # if error file not founds
#     # if try failed except block will work and create new file
#     file = open("Day30/a_file.txt", "w")
#     file.write("Something")
# except KeyError:  # if error keyError show this
#     print("That key does not exist.")
# else:
#     content=file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")

height=float(input("Height:"))
weight=float(input("weight:"))

if height>3:
    raise ValueError("Human Height should not be over 3 meters.")
bmi= weight/height**2
print(bmi)