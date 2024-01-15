import turtle
import pandas

screen = turtle.Screen()
screen.title("Can you Guess all 50 States")
img = "blank_states_img.gif"
screen.addshape(img)
screen.tracer(0)

turtle.shape(img)

#below is code for obtaining coordinates on the background
# def get_mouse_click(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
#END of background coordinates code

game_data = pandas.read_csv("50_states.csv")
states_list = game_data["state"].to_list()
print(states_list)
correct_states = []
while len(correct_states) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(correct_states)} of 50 Guessed",
                                    prompt="What's another state name?").title()
    #now answer state is equivilent to what the user typed in
    if answer_state == None or answer_state == "Exit":
        missing_states = [state for state in states_list if state not in correct_states] #list comprehension
        # for state in states_list:
        #     if state not in correct_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        if answer_state in states_list:
            t = turtle.Turtle()
            t.hideturtle()
            t.up()
            state_data = game_data[game_data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())
            correct_states.append(state_data.state.item())



screen.exitonclick()