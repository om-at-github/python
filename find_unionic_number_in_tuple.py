## python find_unionic_number_in_tuple.py

t1 = [1,3,4,5,6,7,7,9]
list = []
for a in t1 :
    if a not in list :
        list.append(a)
      
print(list)

## second method
for a in t1:
    if a not in list:
        list.push(a)