# Write a Python program to calculate the area of a trapezoid 


import math

def main():
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))
    d = float(input("Enter the fourth side: "))
    s = (a + b + c + d) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c) * (s - d))
    print("The area of the trapezoid is: ", area)

main()