from tkinter import *
from tkinter import messagebox
from pass_generator import password_generator

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    password_entry.insert(0, password_generator())
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_okay = messagebox.askokcancel(title=website, message="These are the details enterd: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if is_okay:
        if len(password) < 7 or len(website) < 4 or email < 6:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

#logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row= 1)

email_label = Label(text="E-mail: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

#entries
website_entry = Entry(width = 35)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width = 35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sam_ricks99@yahoo.com")

password_entry = Entry(width = 20)
password_entry.grid(column=1, row=3)

#buttons
add_button = Button(text="Add", width=35)
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(command=save)

gen_pass_button = Button(text="Generate Pass", command=gen_pass)
gen_pass_button.grid(column=2, row=3)

window.mainloop()