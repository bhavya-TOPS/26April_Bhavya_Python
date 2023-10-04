# Write a Python program to read a random line from a file


import random

def read_random_line(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return random.choice(lines)
read_random_line()