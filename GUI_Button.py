# python GUI_Button.py

from tkinter.simpledialog import askinteger,askfloat,askstring
from tkinter import *
from tkinter import messagebox
top = Tk()

top.geometry("100x100")
def show():
   num = askinteger("Input", "Input an Integer")
   floats = askfloat("Input", "Input an Float")
   Strings = askstring("Input", "Input an String")
   print(num)
   print(floats)
   print(Strings)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

top.mainloop()