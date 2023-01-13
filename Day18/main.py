from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(8)
my_turtle.speed("fastest")

colors = ["black", "yellow", "red", "blue", "gray", "green",
          "tomato", "orange", "navy", "IndianRed", "wheat", "SeaGreen"]
directions = [0, 90, 180, 270]
line_width = [10, 30]

# for _ in range(4):
#     my_turtle.right(90)
#     my_turtle.forward(100)


# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360/num_sides
#         my_turtle.forward(100)
#         my_turtle.right(angle)

# for nu in range (3,15):
#     draw_shape(nu)


def random_walk(steps):
    for _ in range(steps):
        my_turtle.forward(random.choice(line_width))
        my_turtle.color(random.choice(colors))
        my_turtle.setheading(random.choice(directions))


random_walk(200)


my_screen = Screen()
my_screen.exitonclick()
