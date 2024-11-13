# GUI_hello_world.py

from tkinter.simpledialog import askstring
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("500x500")
def helloCallBack():
   msg=messagebox.showinfo( "Hello Python","Hello World")
B = Button(top, text ="Hello", command = helloCallBack ,justify=CENTER)
B.place(x=50,y=50)
top.mainloop()