with open("Day24/my_file.txt") as file:
    content = file.read()
    print(content)
with open("Day24/my_file.txt",mode="a") as file: # w delete previously content a protects old one
    file.write("\nNew content")

# to Create new file use w
with open("Day24/new_file.txt",mode="w")as new_file:
    new_file.write("This is my new file")