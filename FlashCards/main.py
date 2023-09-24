import tkinter
import pandas
import random

IMAGES_FILEPATH = "./images/"
DATA_FILEPATH = "./data/"
BACKGROUND_COLOR = "#B1DDC6"
TIMER_MSEC = 3000

flash_card_data = []
current_card = {}
timer_function = None

try:
    data_df = pandas.read_csv(DATA_FILEPATH + "words_to_learn.csv")
except FileNotFoundError:
    data_df = pandas.read_csv(DATA_FILEPATH + "french_words.csv")
# orient="records" will produce a list of dictionaries
# one row per dictionary
# number of key, value pairs in each dictionary equal to the number of columns
# where key is the name of the column and value is the entry in that particular row
flash_card_data = data_df.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def next_card():
    global current_card, timer_function
    if timer_function is not None:
        window.after_cancel(timer_function)
    current_card = random.choice(flash_card_data)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    timer_function = window.after(TIMER_MSEC, flip_card)


def tick_button_press():
    global data_df
    flash_card_data.remove(current_card)
    data_df = pandas.DataFrame(flash_card_data)
    data_df.to_csv(DATA_FILEPATH+"words_to_learn.csv", index=False)
    next_card()


window = tkinter.Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tkinter.Canvas()

canvas.config(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

card_front_img = tkinter.PhotoImage(file=IMAGES_FILEPATH+"card_front.png")
card_back_img = tkinter.PhotoImage(file=IMAGES_FILEPATH+"card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))


tick_img = tkinter.PhotoImage(file=IMAGES_FILEPATH+"right.png")
cross_img = tkinter.PhotoImage(file=IMAGES_FILEPATH+"wrong.png")

cross_button = tkinter.Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR)
cross_button.grid(row=1, column=0)
cross_button.config(command=next_card)

tick_button = tkinter.Button(image=tick_img, highlightthickness=0, bg=BACKGROUND_COLOR)
tick_button.grid(row=1, column=1)
tick_button.config(command=tick_button_press)

next_card()

window.mainloop()
