# we are using the blank_states_img.gif beacuse turtle will only work on gifs
# Turtle won't work on Jpeg,png etc...

import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle_obj = Turtle()


screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle_obj.shape(image)

data = pandas.read_csv("50_states.csv")
all_state_names = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    #TODO 1: Convert the guess to Title Case
    guessed_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_state_names)} states are Correct"
                                    ,prompt="What's the state name?").title()
    print(guessed_state)

    if guessed_state == 'Exit':
        missing_states = []
        for state in all_state_names:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('learn_missing_states.csv')
        break

    #TODO 2: Check if the guess in 50 states
    if guessed_state in all_state_names:

        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        guess_state_data = data[guessed_state == data.state]
        writer.goto(guess_state_data.x.item(), guess_state_data.y.iloc[0])
        writer.write(arg=guessed_state, align="center", font=('Arial', 8, 'normal'))

        guessed_states.append(guessed_state)







