# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

string1 = input("Enter a string1: ")

string2 = input("Enter a string2: ")

print("string1, string2")

print("string before swap: ",string1," ",string2)

str1 = string2[:2] + string1[2:]
str2 = string1[:2] + string2[2:]

print("string after swap: ",str1," ",str2)