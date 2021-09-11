from turtle import Screen, Turtle

import pandas
import pandas as pd
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()




screen = Screen()
item = Turtle()
state_name = Turtle()

image = "blank_states_img.gif"
screen.addshape(image)
screen.title("U.S States Game")
item.shape(image)


data = pd.read_csv("50_states.csv")


correct = 0
state_guessed = []


while len(state_guessed) < 50:

    answer_state = screen.textinput(title=f"{len(state_guessed)}/50 Guess the State\n correct {correct}",
                                    prompt= "Tell me an State!.").title()
    all_states = data.state.to_list()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in state_guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("study.csv")
        break

    if answer_state in all_states:

        one_state = data[data["state"] == answer_state]
        x = data.loc[data["state"] == answer_state, "x"]
        y = data.loc[data["state"] == answer_state, "y"]
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(int(x), int(y))
        state_name.write(answer_state, font=("Arial", 10, "normal"))
        state_guessed.append(answer_state)
















