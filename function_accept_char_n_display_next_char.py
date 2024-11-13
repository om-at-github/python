# python function_accept_char_n_display_next_char.py
# . Write a function, which accepts a character and integer n as parameter and displays the next n characters. 

def nextchar(num):
    if num % 2 == 0:
        return 1
    else:
        return 0 
ch = input("enter the character = ")
num = chr(ord(ch)+1)
print("next character = ",num) 
