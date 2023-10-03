# Write a Python program to test whether a passed letter is a vowel or
# not.

def is_vowel(letter):
    vowels = ["a", "e", "i", "o", "u"]
    if letter in vowels:
        print("True")
    else:
        print("False")
    
letter = input("Enter a letter: ")

is_vowel(letter)
