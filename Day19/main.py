from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()


def move_forwards():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.backward(10)


def turn_right():
    new_heading = my_turtle.heading()-10
    my_turtle.setheading(new_heading)


def turn_left():
    new_heading = my_turtle.heading()+10
    my_turtle.setheading(new_heading)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_screen.listen()
my_screen.onkey(move_forwards, "w")
my_screen.onkey(move_backwards, "s")
my_screen.onkey(turn_right, "d")
my_screen.onkey(turn_left, "a")
my_screen.onkey(clear, "c")

my_screen.exitonclick()