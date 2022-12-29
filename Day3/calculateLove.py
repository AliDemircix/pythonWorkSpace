print("Welcome to the Love Calculator")

man_name = input("What is man name? \n")
woman_name = input("What is woman name? \n")
trueText = "true"
loveText = "love"
true_count = 0
love_count = 0

names = man_name+" "+woman_name
lowercased_names = names.lower()

for letter in trueText:
    true_count += lowercased_names.count(letter)
for letter in loveText:
    love_count += lowercased_names.count(letter)
print(str(true_count)+str(love_count))
