#Write a Python program to print all unique values in a dictionary

dict = {'a': 1, 'b': 2, 'c':3}

unique_values = set(dict.values())

for value in unique_values:
    print(value)
    