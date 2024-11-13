# python reverse_num.py 
#  Write a program to accept an integer and reverse the number.

num = input ("enter the number")
n = int(num)
rev = 0

for num in num:
    match num:
        case '0' : print("zero")
        case '1' : print("one")
        case '3' : print("three")
        case '4' : print("four")
        case '5' : print("five")
        case '6' : print("six")
        case '7' : print("seven")
        case '8' : print("eight")
        case '9' : print("nine")

print ("#########reverse######")
while n>0:
    rem = n%10
    rev = rev*10 + rem
    n = n//10

print("reverse of a number is",rev)