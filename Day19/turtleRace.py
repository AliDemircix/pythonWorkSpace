from turtle import Turtle, Screen
import random
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bid = my_screen.textinput(
    title="Bid now...!!! ", prompt="Which turtle will win the race? Enter a color: ")

y_positions = [-70, -40, -10, 20, 50, 80,110]
colors = ["red", "yellow", "blue", "orange", "green", "purple","tomato"]
all_turtles = []
is_race_on = False
for turtle_index in range(0, 7):

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bid:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if turtle.color() == user_bid:
                print("CONGRATS YOU WIN")
            else:
                print(f"YOU LOST...{turtle.color()} win.")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

my_screen.exitonclick()
