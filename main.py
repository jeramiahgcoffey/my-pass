from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw_letters = [random.choice(letters) for _ in range(nr_letters)]
    pw_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pw_nums = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = pw_letters + pw_symbols + pw_nums
    random.shuffle(password_list)

    password = "".join(password_list)
    pw_entry.delete(0, END)
    pw_entry.insert(0, password)
    pyperclip.copy(password)

    messagebox.showinfo(message="Your generated password has\n"
                                "been copied to the clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add(event=None):
    website = website_entry.get().title()
    email = email_entry.get()
    pw = pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pw
        }
    }

    if website == "" or email == "" or pw == "":
        messagebox.showwarning(message="Please complete all fields")
    else:
        is_ok = messagebox.askyesno(message=f"{website}\n\nUsername: {email} \nPassword: {pw} \n \nIs it okay to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    # Add updated data to data_file
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                pw_entry.delete(0, END)


# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #
def search():
    website = website_entry.get().title()

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            # for key, value in data.items():
            if website in data:
                email_match = data[website]["email"]
                pw_match = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Username: {email_match} \n"
                                                           f"Password: {pw_match}")
            else:
                messagebox.showerror(message="Record not found")
    except FileNotFoundError:
        messagebox.showerror(message="Record not found")


# ---------------------------- UI SETUP ------------------------------- #
app = Tk()
app.title("Password Manager")
app.config(padx=50, pady=50)
app.minsize(width=100, height=100)
app.eval('tk::PlaceWindow . center')
app.bind('<Return>', add)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=E)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky=E)

email_entry = Entry(width=21)
email_entry.grid(row=2, column=1)

pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0, sticky=E)

pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)

gen_pw = Button(text="Generate Password", command=generate_pw)
gen_pw.grid(row=3, column=2)

add_button = Button(text="Add", width=22, command=add, pady=5)
add_button.grid(row=4, column=1, pady=10)

search_button = Button(text="Search Records", width=13, command=search)
search_button.grid(row=1, column=2)

app.mainloop()
