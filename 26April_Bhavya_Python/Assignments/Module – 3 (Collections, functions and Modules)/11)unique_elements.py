# Write a Python function that takes a list and returns a new list with unique
# elements of the first list. 


def main():

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 2]

    print(lst)

    new_lst = list(set(lst))
    print(new_lst)
    return new_lst

if __name__ == '__main__':
    main()
    