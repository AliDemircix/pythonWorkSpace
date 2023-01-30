import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "Day25/usgame/us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

data=pd.read_csv("Day25/usgame/us-states-game-start/50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 State was Correct",prompt="What's another states name?").title() # title makes all word first letter capitalize

    if answer_state=="Exit":
        # missing_states=[]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states=[state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Day25/usgame/us-states-game-start/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        user_type= data[data.state==answer_state]
        t.goto(int(user_type.x),int(user_type.y))
        # t.write(user_type.state.item())
        t.write(answer_state)


turtle.mainloop() # keep screen open


