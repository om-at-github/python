# python GUI_ex1.py
# Write Python GUI program to take accept your birthdate and output your age when a button is pressed.

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birth_year = int(entry_year.get())
        persent_year = datetime.now().year
        age = persent_year - birth_year
        messagebox.showinfo("Age", age)
    except ValueError:
        mes=messagebox.showerror("invalide year enter, retry again")

root = tk.Tk()
root.title("Calculate_age")

label_year = tk.Label(root,text="Enter the brith year")
label_year.pack(pady=10)

entry_year = tk.Entry(root)
entry_year.pack(pady=10)

Button_age = tk.Button(root ,text="age" ,command=calculate_age )
Button_age.pack(pady=10)

root.mainloop()
