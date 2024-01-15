import json
import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_pass():
    #list_comprehension = [new_item for item in list]
    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_numbers + pass_symbols
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    pass_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    website = site_entry.get()
    username = name_entry.get()
    passw = pass_entry.get()
    new_data = {
        website.title(): {
            "email":username,
            "password":passw,
        }
    }

    if website != "" and username != "" and passw != "":
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Is the following okay to save?\nSite: {website}\n"
                                                          f"Username/Email: {username}\nPassword: {passw}")
        if is_ok:
            try:
                with open('pass_data.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('pass_data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)

                with open('pass_data.json', 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                site_entry.delete(0, 'end')
                pass_entry.delete(0, 'end')
    else:
        messagebox.showinfo(title="Missing Info", message="Please do NOT leave any fields blank.")

# ---------------------------- SEARCH PASS ------------------------------- #
def search():
    try:
        with open('pass_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Missing Data File", message="There is no data file generated yet.\nPlease add a password entry in order to use search.")
    else:
        what_to_look_for = site_entry.get().title()
        if what_to_look_for in data:
            email = data[what_to_look_for]['email']
            passw = data[what_to_look_for]['password']
            messagebox.showinfo(title=what_to_look_for, message=f"Email: {email}\nPassword: {passw}")
        else:
            messagebox.showinfo(title="Error", message=f"No existing entries match {what_to_look_for}.")

# ---------------------------- UI SETUP ------------------------------- #
screen = tkinter.Tk()
screen.title("Pass Manager")
screen.config(padx=20, pady=20)
#canvas, w200, h200, pad20
img = tkinter.PhotoImage(file='logo.png')
logo = tkinter.Canvas(width=200, height=200)
logo.create_image(100, 100, image=img)
logo.grid(row=0, column=1)

site_lbl = tkinter.Label(text='Website:')
site_lbl.grid(row=1, column=0, sticky=['E',])

site_entry = tkinter.Entry(width=35)
site_entry.grid(row=1, column=1, columnspan=2)
site_entry.focus()

site_search_btn = tkinter.Button(text='Search', command=search)
site_search_btn.grid(row=1, column=2)

name_lbl = tkinter.Label(text="Email/Username:")
name_lbl.grid(row=2, column=0)

name_entry = tkinter.Entry(width=35)
name_entry.insert(0,"d@gmail.com")
name_entry.grid(row=2, column=1, columnspan=2)

pass_lbl = tkinter.Label(text="Password:")
pass_lbl.grid(row=3, column=0)

pass_entry = tkinter.Entry(width=30)
pass_entry.grid(row=3, column=1)

gen_pass_btn = tkinter.Button(text="Generate & Copy Password", command=gen_pass)
gen_pass_btn.grid(row=3, column=2)

add_btn = tkinter.Button(text="Add", width=36, command=add_pass)
add_btn.grid(row=4, column=1, columnspan=2)


screen.mainloop()