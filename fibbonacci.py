def fibbo(n):
    if n == 1 or n==2:
        return 1
    else :
        return fibbo(n-1)+fibbo(n-2) 

n = int(input("enter the number - "))
fibbo_serier = fibbo(n)
print("fibbo series = ", fibbo_serier)