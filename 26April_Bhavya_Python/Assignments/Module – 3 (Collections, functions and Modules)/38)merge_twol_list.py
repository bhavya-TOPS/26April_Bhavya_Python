# Write a Python script to merge two Python dictionaries


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

merge_two_dicts()