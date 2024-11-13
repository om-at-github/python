# python function_prime_num_check.py

# Write a function isPrime, which accepts an integer as parameter and returns 1 if the number 
# is prime and 0 otherwise. Use this function in main to display the first 10 prime numbers. 

def isPrime(num):
    flag=0
    if num == 2:
        print("the no is prime")
    else:
        for i in range(2,(num//2)+1):
            if num % i == 0:
                flag = 1
                break
        if flag == 1:
            print("the no not is prime")
        else:
            print("the no is prime")

num=int(input("enter the number = "))            
isPrime(num)