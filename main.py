from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_button():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    #password_letters = [random.choice(letters) for i in range(nr_letters)]
    #password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    #password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(letters)
    random.shuffle(numbers)
    random.shuffle(symbols)

    password_list = [n for n in letters[:nr_letters]] + [n for n in symbols[:nr_symbols]] + [n for n in numbers[:nr_numbers]]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button():
    website_str = website_entry.get()
    email_str = email_entry.get()
    password_str = password_entry.get()

    if len(website_str) == 0 or len(email_str) == 0 or len(password_str) == 0:
        messagebox.showwarning(title="Warning", message="Don't leave empty space")

    else:
        is_ok = messagebox.askokcancel(title=website_str, message=f'These are details entered: \nEmail: {email_str}\nPassword: {password_str}'
                                                      f'\nIs it okay to save?')
        if is_ok:
            f = open('data.txt', 'a')
            f.write(f"{website_str} | {email_str} | {password_str} \n")
            f.close()

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Naru's password")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="website")
website_label.grid(row=1, column=0)

email_label = Label(text="email/username")
email_label.grid(row=2, column=0)

password_label = Label(text="password")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dummy@dummy.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, padx=(12,0))

generate_password_button = Button(text="generate password", command=generate_password_button)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="add", width=36, command=add_button)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()
