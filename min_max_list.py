## python min_max_list.py

arr = [3,4,1,2,6,8]

minn = arr[0]
maxx = arr[0]
for a in arr:
    if a < minn:
        minn = a

    if a > maxx:
        maxx = a

print(f'Minimum value in a list is {minn}')
print(f'Maximum value in a list is {maxx}')


print("min max using inbuilt function")
print(min(arr))
print(max(arr))

