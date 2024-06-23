import tkinter as tk
from tkinter import messagebox
import random
import string

# Password generating function
def generate_password():
    length = int(length_entry.get())
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()
    
    if not (include_upper or include_lower or include_digits or include_special):
        messagebox.showerror("Error", "You must choose at least one type of sign")
        return
    
    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Creating the main window
root = tk.Tk()
root.title("Password Generator")

# Label and text field for password length
tk.Label(root, text="Password length:").grid(row=0, column=0, sticky=tk.W)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Checkbuttons for different types of characters
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Capital letters", variable=upper_var).grid(row=1, column=0, sticky=tk.W)
tk.Checkbutton(root, text="Small letters", variable=lower_var).grid(row=1, column=1, sticky=tk.W)
tk.Checkbutton(root, text="Digits", variable=digits_var).grid(row=2, column=0, sticky=tk.W)
tk.Checkbutton(root, text="Special characters", variable=special_var).grid(row=2, column=1, sticky=tk.W)

# Text field for the generated password
password_entry = tk.Entry(root)
password_entry.grid(row=3, column=0, columnspan=2)

# Password generation button
generate_button = tk.Button(root, text="Generuj hasło", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2)

# Run app loop
root.mainloop()
