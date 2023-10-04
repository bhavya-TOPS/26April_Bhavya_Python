# Write a Python function to calculate the factorial of a number (a
# nonnegative integer) 

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

factorial(5)