# python accept_char_digit_sbybols_print_1_2_3.py
# Write a function that accepts a character as parameter and returns 1 if it is an alphabet, 2 if it 
#is a digit and 3 if it is a special symbol. In main, accept characters till the user enters EOF and use 
#the function to count the total number of alphabets, digits and special symbols entered.  

def checkChar(ch) :
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        return 1
    elif ch >= '0' and ch <= '9':
        return 2
    else:
        return 3


ch = input("enter a character")
val = checkChar(ch)
if val == 1:
    print(f"{ch} is a alphabet")
elif val == 2:
    print(f"{ch} is a number")
else:
    print(f"{ch} is a special symbol")
