# python function_even_odd.py #

#  Write a function isEven, which accepts an integer as parameter and returns 1 if the number is 
#even, and 0 otherwise. Use this function in main to accept n numbers and ckeck if they are even 
# or odd. 

def evenodd(num):
    if num % 2 == 0:
        return 1
    else:
        return 0

num=int(input("enter the number"))
val=evenodd(num)
if(val==1):
    print("no is even")
else:
    print("no is odd")

      