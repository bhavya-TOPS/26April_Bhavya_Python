# Write a Python function to get the largest number, smallest num and sum
# of all from a list. 

list = []

number = int(input("How many elements: "))

for a in range(number):
    items = int(input("Enter an items: "))

    list.append(items)

print("Maximum element in the list is :", max(list))
print("Minimum element in the list is :", min(list))
print("Sum of all the elements of list is :",sum(list))

