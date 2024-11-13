# python GUIex_calculater.py

import tkinter as tk

def click(event):
    current_text = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for displaying the input and result
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Create number and operator buttons individually
button_1 = tk.Button(root, text='7', width=5, height=2, font=("Arial", 18))
button_1.grid(row=1, column=0)
button_1.bind("<Button-1>", click)

button_2 = tk.Button(root, text='8', width=5, height=2, font=("Arial", 18))
button_2.grid(row=1, column=1)
button_2.bind("<Button-1>", click)

button_3 = tk.Button(root, text='9', width=5, height=2, font=("Arial", 18))
button_3.grid(row=1, column=2)
button_3.bind("<Button-1>", click)

button_divide = tk.Button(root, text='/', width=5, height=2, font=("Arial", 18))
button_divide.grid(row=1, column=3)
button_divide.bind("<Button-1>", click)

button_4 = tk.Button(root, text='4', width=5, height=2, font=("Arial", 18))
button_4.grid(row=2, column=0)
button_4.bind("<Button-1>", click)

button_5 = tk.Button(root, text='5', width=5, height=2, font=("Arial", 18))
button_5.grid(row=2, column=1)
button_5.bind("<Button-1>", click)

button_6 = tk.Button(root, text='6', width=5, height=2, font=("Arial", 18))
button_6.grid(row=2, column=2)
button_6.bind("<Button-1>", click)

button_multiply = tk.Button(root, text='*', width=5, height=2, font=("Arial", 18))
button_multiply.grid(row=2, column=3)
button_multiply.bind("<Button-1>", click)

button_1_2 = tk.Button(root, text='1', width=5, height=2, font=("Arial", 18))
button_1_2.grid(row=3, column=0)
button_1_2.bind("<Button-1>", click)

button_2_2 = tk.Button(root, text='2', width=5, height=2, font=("Arial", 18))
button_2_2.grid(row=3, column=1)
button_2_2.bind("<Button-1>", click)

button_3_2 = tk.Button(root, text='3', width=5, height=2, font=("Arial", 18))
button_3_2.grid(row=3, column=2)
button_3_2.bind("<Button-1>", click)

button_minus = tk.Button(root, text='-', width=5, height=2, font=("Arial", 18))
button_minus.grid(row=3, column=3)
button_minus.bind("<Button-1>", click)

button_0 = tk.Button(root, text='0', width=5, height=2, font=("Arial", 18))
button_0.grid(row=4, column=0)
button_0.bind("<Button-1>", click)

button_dot = tk.Button(root, text='.', width=5, height=2, font=("Arial", 18))
button_dot.grid(row=4, column=1)
button_dot.bind("<Button-1>", click)

button_equal = tk.Button(root, text='=', width=5, height=2, font=("Arial", 18))
button_equal.grid(row=4, column=2, columnspan=1)
button_equal.bind("<Button-1>", click)

button_plus = tk.Button(root, text='+', width=5, height=2, font=("Arial", 18))
button_plus.grid(row=4, column=3)
button_plus.bind("<Button-1>", click)

# Special button for clearing the entry widget
button_clear = tk.Button(root, text='C', width=22, height=2, font=("Arial", 18))
button_clear.grid(row=5, column=0, columnspan=4)
button_clear.bind("<Button-1>", click)

# Start the Tkinter event loop
root.mainloop()
