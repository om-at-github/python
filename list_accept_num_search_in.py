## python list_accept_num_search_in.py
## accept list, in list search num

list = [1,3,4,2,4,2,5,6,7,8,9,10]
num = int(input("enter the number = "))
list.count(num)
if num in list :
    print("1")
else :
    print("-1")    