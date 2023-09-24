import tkinter


def button_clicked():
    my_label.config(text=my_entry.get())


# # # Create Window # # #
window = tkinter.Tk()
window.title("My First GUI Program")
# Edit Size of Window
# window.minsize()
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# # # Create Label # # #
# my_label = tkinter.Label(text="I am a Label")
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# # positional argument changing of Label Text
# my_label["text"] = "I am a Label"
# # key word argument changing of label text
# my_label.config(text="I am a Label")
# my_label = tkinter.Label(text="I am a Label", font=("Arial, 24"))
# # Display Label on Window
# my_label.pack(side="left")
# my_label.pack(side="bottom")
# my_label.pack(expand=True)
# # Positioning Managers for Widgets: Pack, Place, Grid
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(row=0,column=0)
my_label.config(padx=10, pady=10)

# # # Create Button # # #
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(row=1,column=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(row=0,column=2)

# # # Create Entry # # #
# # It is a  Single Line Text Box
my_entry = tkinter.Entry()
my_entry.config(width=15)
# my_entry.pack()
my_entry.grid(row=2,column=3)


window.mainloop()
