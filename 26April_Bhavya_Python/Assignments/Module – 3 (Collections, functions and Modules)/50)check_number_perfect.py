# Write a Python function to check whether a number is perfect or not


def is_perfect(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False

print(is_perfect(28))