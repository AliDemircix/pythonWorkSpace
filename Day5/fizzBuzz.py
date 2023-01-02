# If divided 3 say fizz , divided 5 say buzz , divided both 3 and 5 say fizzbuzz

for number in range(1,101):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)