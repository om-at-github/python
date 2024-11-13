# GUI_Simple_Color_Changer.py

import tkinter as tk
import random

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black', 'white']

def change_color():
    color = random.choice(colors)
    root.config(bg=color)
    root.after(1000,change_color)

root = tk.Tk()
root.geometry("200x200")
root.title("Color Changer")

#button = tk.Button(root, text="Change Color", command=change_color, font=('Arial', 16))
#button.pack(pady=20)
change_color()

root.mainloop()
