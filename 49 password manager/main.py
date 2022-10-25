from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
               "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
               "z", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ["0", '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', "$", "%", "^", "&", '*', "(", ")", "+", "_", "-"]

    # print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(0, nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(0, nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(0, nr_symbols)]

    created_password = password_symbols + password_numbers + password_letters
    random.shuffle(created_password)
    password = "".join(created_password)
    password_e.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_e.get()
    email = email_username_e.get()
    password = password_e.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='opps', message="Please make sure you haven't left any fields empty.")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                                f"Password: {password}\nIs it okay to save?")

        if is_okay:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                    # data_file.write(f"{website} | {email} | {password}\n")
            finally:
                website_e.delete(0, END)
                password_e.delete(0, END)


def search():
    website = website_e.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='opps', message="File not found")
    else:
        if website in data:
            passw = data[website]["password"]
            email = data[website]["email"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {passw}")
            pyperclip.copy(passw)
        else:
            messagebox.showinfo(title='opps', message=f"{website} not found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_l = Label(text="Website:")
website_l.grid(column=0, row=1)

email_username_l = Label(text="Email/Username:")
email_username_l.grid(column=0, row=2)

password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

website_e = Entry(width=33)
website_e.grid(column=1, row=1)
website_e.focus()

email_username_e = Entry(width=52)
email_username_e.grid(column=1, row=2, columnspan=2)
email_username_e.insert(index=0, string="taank.kritika@gmail.com")

password_e = Entry(width=33)
password_e.grid(column=1, row=3)

search = Button(text="Search", width=15, command=search)
search.grid(column=2, row=1)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=45, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
