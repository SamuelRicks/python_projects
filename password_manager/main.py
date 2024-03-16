from tkinter import *
from tkinter import messagebox
from pass_generator import password_generator
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    password_entry.insert(0, password_generator())
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if len(password) < 7 or len(website) < 4 or len(email) < 6:
        messagebox.showinfo(title="Oops", message="Please make sure that you have not left any on the fields blank.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)
        else:
            data.update(new_data, data_file)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# -------------------------- FIND PASSWORD ---------------------------- #
            
def find_password():
    website  = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="No website", message=f"Sorry, the information for {website} is not in you data base")
    finally:
        website_entry.delete(0, END)



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
website_entry = Entry(width = 21)
website_entry.grid(column=1, row=1)

email_entry = Entry(width = 36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sam_ricks99@yahoo.com")

password_entry = Entry(width = 21)
password_entry.grid(column=1, row=3)

#buttons
add_button = Button(text="Add", width=35)
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(command=save)

gen_pass_button = Button(text="Generate Pass", command=gen_pass)
gen_pass_button.grid(column=2, row=3)

search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()