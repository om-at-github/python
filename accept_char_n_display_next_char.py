# Write a program to accept a character, an integer n and display the next n characters. 
# python accept_char_n_display_next_char.py
# def evenodd(num):
    if num % 2 == 0:
        return 1
    else:
        return 0  
ch = input("enter the character")
x1 = chr(ord(ch)-1)
x2 = chr(ord(ch)+1)
print("next character",x2)
print("prev character",x1)