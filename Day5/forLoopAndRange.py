# For loop with range(1,10) => not include 10

for number in range(1, 10, 2):  # if you want to make a step add 3.parameter range(1,10,2)
    print(number)  # will print 1,2,3,4,5,6,7,8,9

total=0
for number in range(0,101,2):
    total+=number
print(total)