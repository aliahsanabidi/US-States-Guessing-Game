import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

#Creating the map image and setting it as a new turtle on screen
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

#Reading names of the states from the states file using Pandas
states_name = pandas.read_csv("50_states.csv")

#Converting the series data to list so that we can check if the name entered is in the list of states.
data_list = states_name.state.to_list()

#Checking if the name entered is in the list of states we created earlier and then
#creating a turtle which will write the name of state on relevant x & y coordinates.

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 guessed correct!", prompt="What's the name of next state?").title()
    # getting hold of the row which matches the name of state entered by user.
    input_state_name = states_name[states_name["state"] == answer_state]
    #Breaking the loop when player writes exit and add to the list of missing states.
    if answer_state == "Exit":
        #Here we made use of list comprehension to create a new list from pre-exiting list
        missing_states = [state for state in data_list if state not in guessed_states]
        # missing_states = []
        # for state in data_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        # creating dataframe from missing_states list and converting the dataframe to new CSV file.
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in data_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(input_state_name.x), int(input_state_name.y))
        t.write(input_state_name.state.item(), font=("Times New Roman", 9, "normal"))


#Here we are not using exitonclick method as we need to exit the while loop once the user types
#exit in the text input.
# screen.exitonclick()