import tkinter as tk
from tkinter import messagebox
import random
import string
import json

def generate_password():
    password_length = 12  # You can customize the length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Create a new file if it doesn't exist
                    json.dump({}, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update({website: {"email": username, "password": password}})

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")  # Replace "logo.png" with your image file
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = tk.Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "youremail@example.com")  # You can change this
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = tk.Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
