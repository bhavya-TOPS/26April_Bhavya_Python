# Write a Python program to find the maximum and minimum numbers
# from the specified decimal numbers

def max_min(num):
    max_num = 0
    min_num = 0
    for i in num:
        if i > max_num:
            max_num = i
            min_num = i
            continue
        if i < min_num:
            min_num = i
            max_num = i
            continue
    return max_num, min_num

num = [1.35, 2.5, 3.7, 4.5, 5.5, 6.7]

print(max_min(num))

