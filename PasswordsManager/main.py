import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password_to_file():
    website_name = website_entry.get()
    email_address = email_entry.get()
    password_text = password_entry.get()
    if website_name != "" and email_address != "" and password_text != "":
        new_data = {
            website_name: {
                "email": email_address,
                "password": password_text
            }
        }
        is_ok = messagebox.askokcancel(title=website_name, message="Are you sure you want to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    # read all the data into a dictionary
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # add new data (dictionary) to the old data (dictionary)
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    # save the updated data back to the json file
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
    else:
        messagebox.showwarning(title="Error", message="Website, Email, and Password can not be empty!")


# ---------------------------- SEARCH PASSwORD ------------------------------- #

def search_password():
    website_name = website_entry.get()
    if website_name != "":
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No data file found")
        else:
            if website_name in data:
                email_address = data[website_name]["email"]
                password_text = data[website_name]["password"]
                message_to_display = f"Website: {website_name}\nEmail/Username: {email_address}\n" \
                                     f"Password: {password_text}\nPassword is copied on clipboard."
                messagebox.showinfo(title="Login Info", message=message_to_display)
                pyperclip.copy(password_text)
            else:
                messagebox.showwarning(title="Error", message="No details for the website exists")
    else:
        messagebox.showwarning(title="Error", message="Please enter a website name to initiate search")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website: ")
website_label.grid(row=1, column=0, sticky="w")

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(row=2, column=0, sticky="w")

password_label = tkinter.Label(text="Password: ")
password_label.grid(row=3, column=0, sticky="w")

website_entry = tkinter.Entry(width=40)
website_entry.grid(row=1, column=1, sticky="ew")
website_entry.focus()

email_entry = tkinter.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "shahidhasankhan6@gmail.com")

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

search_button = tkinter.Button(text="Search", width=14, command=search_password)
search_button.grid(row=1, column=2, sticky="ew")

generate_password_button = tkinter.Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew")

add_button = tkinter.Button(text="Add", width=36, command=save_password_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
