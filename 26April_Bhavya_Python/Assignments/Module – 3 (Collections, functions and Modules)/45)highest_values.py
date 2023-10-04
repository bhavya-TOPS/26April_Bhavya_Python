# Write a Python program to find the highest 3 values in a dictionary

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
print(max(d.values()))
print(max(d.values(), key=d.get))
print(max(d.values(), key=d.get, default=0))

