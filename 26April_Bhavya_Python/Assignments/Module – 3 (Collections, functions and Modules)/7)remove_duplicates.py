# Write a Python program to remove duplicates from a list

list = [10,25,10,52,20,10]

duplicates_items = set()

unique_items = []

for x in list:
    if x not in duplicates_items:
        unique_items.append(x)
        duplicates_items.add(x)

print(duplicates_items)
