# Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5.

def is_five(num1, num2):
    if num1 == num2:
        print("True")
    elif num1 + num2 == 5:
        print("True")
    elif num1 - num2 == 5:
        print("True")
    else:
        print("False")
    
num1 = int(input("Enter a number: "))

num2 = int(input("Enter another number: "))

is_five(num1, num2)
