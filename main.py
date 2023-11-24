import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
turtle.hideturtle()

data = pandas.read_csv("50_states.csv")
states_list = data.state.tolist()
coor_x = data.x.tolist()
coor_y = data.y.tolist()

correct_list = []
while len(correct_list) <= 50:
    answer_state = screen.textinput(title=f"{len(correct_list)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [states for states in states_list if states not in correct_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for index in range(len(states_list)):
        if states_list[index] == answer_state:
            turtle.penup()
            turtle.goto(coor_x[index], coor_y[index])
            turtle.write(answer_state, align="center", font=("Arial", 12, "normal"))
            correct_list.append(answer_state)


