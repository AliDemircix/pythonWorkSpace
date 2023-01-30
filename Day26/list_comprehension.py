# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n*3 for n in numbers]
print(new_list)

name ="Ali Demirci"
letters_list=[letter for letter in name]
print(letters_list)

#CONDITIONS 
# new_list=[new_item for item in list if test]
names=["Ali","Alex","Carolina","Freddie","Alexsander"]

short_names= [name.lower() for name in names if len(name)<5]
print(short_names)
