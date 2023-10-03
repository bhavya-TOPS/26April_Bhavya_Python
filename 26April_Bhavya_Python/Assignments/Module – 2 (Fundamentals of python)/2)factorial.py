# Write a Python program to get the Factorial number of given number. 

factorials = int(input("Enter a Factorial number:"))

factorial = 1

for i in range(1, factorials + 1):
    factorial = factorial * i
    