# python check_char_uppercase_or_lowercase.py 

ch = str(input("enter the character = "))

if len(ch) <= 1 :
	print("This is a single character or number")
else:
	if ch >= 'A' and ch <= 'Z':
		print("it is uppercase character")
	elif ch >= 'a' and ch <= 'z':
		print("it is lowercase character")
	elif ch >= '0' and ch <= '9':
		print("it is number")
	else:
		print("it number is a character")