# Write a Python program to combine two dictionary adding values for
# common keys

def combine_dict(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'a': 1, 'b': 2}

dict2 = {'c': 3, 'd': 4}

print(combine_dict(dict1, dict2))

combine_dict(dict1, dict2)