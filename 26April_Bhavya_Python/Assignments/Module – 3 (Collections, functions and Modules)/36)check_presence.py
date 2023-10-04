# How Do You Check The Presence Of A Key In A Dictionary

d1 = {'a': 1, 'b': 2, 'c': 3}

print(d1)

if 'a' in d1:
    print('a is present in the dictionary')
    print(d1['a'])
else:
    print('a is not present in the dictionary')