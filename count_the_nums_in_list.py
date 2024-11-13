## python count_the_nums_in_list.py

list = (1,1,2,3,4,5,6,6,6,7,8,5,0,9,0)
for a in list:
    list.count(a)
    a = int(input("enter the number in list = "))
    print(list.count(a))