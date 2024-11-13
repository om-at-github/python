# python GUI_calculaterimport tkinter as tk

import tkinter as tk

def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget to display the calculations
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4).py



# Define the buttons and their layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=calculate).grid(row=row, column=col)
        col += 1
    else:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=lambda b=button: on_button_click(b)).grid(row=row, column=col)
        col += 1
        if col > 3:
            col = 0
            row += 1

# Add a Clear button
tk.Button(root, text='C', width=23, height=2, font=('Arial', 18), command=clear).grid(row=row, column=0, columnspan=4)

# Start the Tkinter main loop
root.mainloop()