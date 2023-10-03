# Write a Python script to concatenate following dictionaries to create a
# new one.

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6}
d3 = {'g': 7, 'h': 8, 'i': 9}
d4 = {'j': 10, 'k': 11, 'l': 12}

print(d1)

print(d2)

print(d3)

print(d4)

print(d1.items() + d2.items() + d3.items() + d4.items())

