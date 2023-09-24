import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

background = Turtle()
background.shape(image)
background.penup()

writing_tool = Turtle()
writing_tool.hideturtle()
writing_tool.penup()


game_data = pandas.read_csv("50_states.csv")
states_list = game_data.state.to_list()

score = 0
already_guessed = []

# continue game till all 50 states have been guessed
while len(already_guessed) < 50:
    user_guess = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()
    # end the game if user types exit
    if user_guess == "Exit":
        # create a csv file with all unguessed states and exit from the game
        # create output list for unguessed states using list comprehension
        unguessed_states = [state for state in states_list if state not in already_guessed]
        # # create output list for unguessed states without using list comprehension
        # unguessed_states = []
        # for state in states_list:
        #     if state not in already_guessed:
        #         unguessed_states.append(state)

        # # to output data without column names just convert list to data frame
        # output_data_df = pandas.DataFrame(unguessed_states)
        # to output data with column names first convert list to dictionary with column names then make data frame
        output_data_dict = {"unguessed states": unguessed_states}
        output_data_df = pandas.DataFrame(output_data_dict)
        output_data_df.to_csv("states_to_learn.csv")
        break
    # check if the user guess is the correct name of a state and that name has not already been guessed
    if user_guess in states_list and user_guess not in already_guessed:
        # adding state to already guessed list
        already_guessed.append(user_guess)
        # Add score
        score += 1
        # Display name of that list on screen
        x_cor = game_data[game_data.state == user_guess].x.item()
        y_cor = game_data[game_data.state == user_guess].y.item()
        # x_cor = game_data[game_data.state == user_guess].x.iloc[0]
        # y_cor = game_data[game_data.state == user_guess].y.iloc[0]
        writing_tool.setpos(x_cor, y_cor)
        writing_tool.write(user_guess)

# screen.mainloop()

# # How to get coordinates of every state on the image
# coordinates_list = []
# def get_mouse_click_coordinates(x_cor, y_cor):
#     coordinates_list.append((x_cor, y_cor))
# turtle.onscreenclick(fun=get_mouse_click_coordinates)
