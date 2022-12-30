fruits = ["Apple", "Banana", "Pear"]

for fruit in fruits:
    print(fruit)

# Create a list including students notes and get average note and print it
students_notes = [90, 84, 84, 66, 70, 88, 96, 84, 28, 50]

# total=0
# average=0

# for note in students_notes:
#     total+=note
# average=total/len(students_notes)
# print(average)
total_notes = sum(students_notes)
average = total_notes/len(students_notes)
print(average)

# find max value and min value in a list

print(max(students_notes), min(students_notes))

highest = 0
min = 101

for note in students_notes:
    if note > highest:
        highest = note
    if note < min:
        min = note
print(highest, min)
