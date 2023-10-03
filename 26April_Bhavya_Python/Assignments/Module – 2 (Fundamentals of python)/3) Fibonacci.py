# Write a Python program to get the Fibonacci series of given range.

numbers = int(input("Enter the number: "))

fib = 0
fib1 = 0
fib2 = 1

while fib1 < numbers:
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib

    print(fib)

