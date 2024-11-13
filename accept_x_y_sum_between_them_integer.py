# python accept_x_y_sum_between_them_integer.py 
# Accept two integers x and y and calculate the sum of all integers between x and y (both inclusive)

x = int(input("enter the number x"))
y = int(input("enter the number y"))
sum = 0
for i in range(x+1,y):
    sum = sum + i

print(sum)