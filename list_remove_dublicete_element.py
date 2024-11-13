## python list_remove_dublicete_element.py
##  Write a program to remove all duplicate elements from an list. 

list = [1,1,1,3,3,2,5,5,6,7,7,7,8,9,0,0,0,1,11,10]

## loop metthod
res = []
for a in list:
    if a not in res:
        res.append(a)

print("list without duplicate", res)

## function method
set(list)
print("list without duplicate",set(list))