from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- SEARCH FUNCTION ---------------------------------- #


def search():
    try:
        with open('data.json', 'r') as data_file:
            data_dict = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message='No information has yet been saved.')
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title='Oops', message='No information has yet been saved.')
    else:
        try:
            if website_entry.get().lower() in data_dict:
                messagebox.showinfo(title=website_entry.get(),
                                    message=f'Email: {data_dict[website_entry.get().lower()]["email"]}\n'
                                            f'Password: {data_dict[website_entry.get().lower()]["password"]}')
        except KeyError:
            messagebox.showinfo(title='Oops', message=f'{website_entry.get()} was not found.')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_data = {
        website_entry.get().lower(): {
            'email': email_entry.get(),
            'password': password_entry.get(),
        }
    }
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title='Empty Fields', message='Please do not leave any fields empty.')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data_dict = json.load(data_file)
                data_dict.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                json.dump(data_dict, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(message='Your information has been saved.')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=3)

website_label = Label(text='Website', font=('Arial', 10))
website_label.grid(column=0, row=1)
website_entry = Entry(width=25, highlightthickness=1, font=('Arial', 10))
website_entry.grid(column=1, row=1, pady=1)
website_entry.focus()

email_label = Label(text='Email/Username', font=('Arial', 10))
email_label.grid(column=0, row=2)
email_entry = Entry(width=41, highlightthickness=1, font=('Arial', 10))
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password', font=('Arial', 10))
password_label.grid(column=0, row=3)
password_entry = Entry(width=25, highlightthickness=1, font=('Arial', 10))
password_entry.grid(column=1, row=3)

search_button = Button(text='Search', width=14, bd=1, command=search)
search_button.grid(column=2, row=1)

generate_password_button = Button(text='Generate Password', bd=1, command=generate)
generate_password_button.grid(column=2, row=3, pady=1)

add_info_button = Button(text='Add', width=41, bd=1, command=save)
add_info_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
