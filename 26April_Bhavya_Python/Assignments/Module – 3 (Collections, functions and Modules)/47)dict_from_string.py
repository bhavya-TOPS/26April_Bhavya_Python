# Write a Python program to create a dictionary from a string

def main():
    string = input("Enter a string: ")
    d = {}
    for i in string:
        d[i] = string.count(i)
    print(d)

main()