# Write a Python program to reverse a tuple

def main():
    tup = (1, 2, 3, 4, 5)
    print(tup)
    tup = tuple(reversed(tup))
    print(tup)
main()