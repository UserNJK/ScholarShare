import tkinter as tk
from tkinter import messagebox

def create_account():
    username = entry1.get()
    password = entry2.get()
    confirm_password = entry3.get()

    if password == confirm_password:
        # Here you would typically add code to create the account in your system
        messagebox.showinfo("Account info", f"Account created for {username}!")
    else:
        messagebox.showinfo("Account info", "Passwords do not match!")

def login():
    username = entry1.get()
    password = entry2.get()

    # Here you would typically add code to check the provided credentials
    messagebox.showinfo("Login info", f"Welcome {username}!")

root = tk.Tk()
root.geometry("300x200")

label1 = tk.Label(root, text="Username")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Password")
entry2 = tk.Entry(root, show="*")
label3 = tk.Label(root, text="Confirm Password")
entry3 = tk.Entry(root, show="*")

create_button = tk.Button(root, text="Create Account", command=create_account)
login_button = tk.Button(root, text="Login", command=login)

# Initially, we hide the "Confirm Password" field
label3.pack_forget()
entry3.pack_forget()

def switch_to_create_account():
    # Show the "Confirm Password" field
    label3.pack()
    entry3.pack()
    root.geometry("300x250")  # Adjust window size

def switch_to_login():
    # Hide the "Confirm Password" field
    label3.pack_forget()
    entry3.pack_forget()
    root.geometry("300x200")  # Adjust window size

# Add buttons to switch between "Create Account" and "Login"
switch_to_create_account_button = tk.Button(root, text="Switch to Create Account", command=switch_to_create_account)
switch_to_login_button = tk.Button(root, text="Switch to Login", command=switch_to_login)

# Pack everything in the right order
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
create_button.pack()
login_button.pack()
switch_to_create_account_button.pack()
switch_to_login_button.pack()

root.mainloop()
