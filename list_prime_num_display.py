## python list_prime_num_display.py
## Write a program to accept n numbers and store all prime numbers in an list called prime. 
## Display this list .

list = [1,3,4,6,5,7,8,9,11,2,4,44,77,0]
prime = []
for a in list :
    flag = 1 if a >=2 else 0
    if a >= 2:
        for i in range (2,a):
            if a % i == 0 :
                flag = 0

    if flag == 1 :
        prime.append(a)

print(prime)