## python in_list_duplicates_num_remove.py
## write a program to accept n numbers in list and remove duplicates from a list.

list = [1,1,1,3,3,2,5,5,6,7,7,7,8,9,0,0,0,1,11,10]
num = int(input("enter the number in list = "))

for num in list:
    list.remove(num)
    print(list)