# Write a Python program to calculate surface volume and area of a
# cylinder

import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = math.pi * radius ** 2 * height

area = math.pi * radius ** 2

print("The volume of the cylinder is: ", volume)

print("The area of the cylinder is: ", area)

