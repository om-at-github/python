## python Check_num_in_range.py

## Write a Python program to check whether a number is in a given range.

number = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if start <= number <= end:
    print(f"{number} is in the range.")
else:
    print(f"{number} is not in the range.")
