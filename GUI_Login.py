## python GUI_Login.py

import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_user.get()
    password = entry_pass.get()
    if username == "user" and password == "pass":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid credentials")

root = tk.Tk()
root.title("Login Form")

tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show='*')
entry_pass.pack(pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

root.mainloop()