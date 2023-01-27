from turtle import Screen

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)



screen.listen()



game_is_on = True



screen.exitonclick()
