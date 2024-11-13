## python accept_string_calculate_num_letters.py

## Write a function accepts a string and calculate the numbers of upper case letters and 
## lower case letters
##  Ex sample: "The quick Brown FOx"
##  output: upper case:4
##          lower case:12.  

def count_case_characters(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    print("No. of Upper case characters:", upper_count)
    print("No. of Lower case characters:", lower_count)

# Example usage:
sample_string = 'The quick Brown Fox'
count_case_characters(sample_string)
