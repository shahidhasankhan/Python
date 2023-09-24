import tkinter


def calculate_km_from_miles():
    miles = miles_input_entry.get()
    km = 0
    if miles != "":
        km = round(float(miles) * 1.609, 2)
    km_display_label.config(text=f"{km}")


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)
# window.minsize(height=200, width=500)

miles_input_entry = tkinter.Entry(width=10)
miles_input_entry.grid(row=0, column=1)
miles_input_entry.focus()

miles_unit_label = tkinter.Label(text="Miles")
miles_unit_label.grid(row=0, column=2)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_display_label = tkinter.Label(text=" 0 ")
km_display_label.grid(row=1, column=1)

km_unit_label = tkinter.Label(text="Km")
km_unit_label.grid(row=1, column=2)

calculate_button = tkinter.Button(text="Calculate", command=calculate_km_from_miles)
calculate_button.grid(row=2, column=1)

window.mainloop()
