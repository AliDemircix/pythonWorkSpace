row1 = ["ππΏ", "ππΏ", "ππΏ"]
row2 = ["ππΏ", "ππΏ", "ππΏ"]
row3 = ["ππΏ", "ππΏ", "ππΏ"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put your baby?")
horizontal = int(position[0])
vertical = int(position[1])
map[vertical-1][horizontal-1]="πΌπ½"
print(f"{row1}\n{row2}\n{row3}")
