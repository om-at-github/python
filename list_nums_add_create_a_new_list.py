## python list_nums_add_create_a_new_list.py
## list out the positive number 

list = [1,2,3,4,5]
res = []

res.append(list[0])

for i in range(1,len(list)):
    sum = list[i] + res[i-1]
    res.append(sum)

print("res=",res)    