# Write a Python program to map two lists into a dictionar

def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10]
    d = dict(zip(l1, l2))
    print(d)

main()