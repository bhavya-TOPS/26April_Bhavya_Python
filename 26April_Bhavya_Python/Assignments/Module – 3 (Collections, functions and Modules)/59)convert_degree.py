# Write a Python program to convert degree to radian



import math

def rad2deg(rad):
    return rad * (180 / math.pi)

def main():
    deg = float(input("Enter the degree: "))
    rad = rad2deg(deg)
    print("The radian is: ", rad)
    print("The degree is: ", rad2deg(rad))
