import pandas
from turtle import Turtle, Screen

data = pandas.read_csv("50_states.csv")

screen = Screen()
screen.title("US State Game")

map = "blank_states_img.gif"

screen.addshape(map)

turtle = Turtle()

turtle.shape(map)

game_status = True

score = 0

guessed_states = []

while game_status:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="Write a state:").title()

    if answer == "Exit":
        missing_states = [_ for _ in data.state if _ not in guessed_states]
        result = pandas.DataFrame(missing_states)
        result.to_csv("Missing_States.csv")
        break

    for state_name in data.state:
        if state_name == answer:
            chosen_state = data[data.state == state_name]
            a = int(chosen_state.x)
            b = int(chosen_state.y)
            state_word = Turtle()
            state_word.hideturtle()
            state_word.penup()
            state_word.goto(a, b)
            state_word.write(f"{state_name}")
            score += 1
            guessed_states.append(state_name)
