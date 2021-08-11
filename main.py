from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
app = Tk()
app.title("Password Manager")
app.config(padx=50, pady=50)
app.eval('tk::PlaceWindow . center')

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=E)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky=E)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0, sticky=E)

pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)

gen_pw = Button(text="Generate Password")
gen_pw.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

app.mainloop()