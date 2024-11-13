## python find_common_num_in_list.py
## find_common_number_in_two_list


list1 = [1,2,3,4,5,9,6,7,8,8]
list2 = [1,5,2,3,45,11,12,33,99]
list3 = []
for a in list1 :
    if a in list2 :
        list3.append(a)
        
        
print(list3)