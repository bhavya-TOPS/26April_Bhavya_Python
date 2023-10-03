# Write a Python script to sort (ascending and descending) a dictionary by
# value

def sort_dict_by_value(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

d = {'a': 1, 'b': 2, 'c': 3}

print(sort_dict_by_value(d))

