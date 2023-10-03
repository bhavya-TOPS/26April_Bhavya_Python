# Write a Python program to print all unique values in a dictionary

programming={
    "Python":100,
    "Java":90,
    "C++":80
}

for language in set(programming.values()):
    print(language.title())
