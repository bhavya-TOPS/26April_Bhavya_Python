# Write a Python program to unzip a list of tuples into individual lists. 

list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

print(list)

list = list(zip(*list))

print(list)

