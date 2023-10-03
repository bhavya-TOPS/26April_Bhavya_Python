# Write a Python program to find the repeated items of a tuple. 

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9,6,5)

for i in tuple:
    if tuple.count(i) > 1:
        print(i, "is repeated")
    else:
        print(i, "is not repeated")