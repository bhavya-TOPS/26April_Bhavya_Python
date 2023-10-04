# Write a Python function to check whether a number is in a given range

def is_in_range(num, min_num, max_num):
    if num >= min_num and num <= max_num:
        return True
    else:
        return False
    
print(is_in_range(10, 0, 10))
