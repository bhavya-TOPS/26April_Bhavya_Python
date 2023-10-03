# Write a Python function that takes a list of words and returns the length
# of the longest one.

def longest_word(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

words = input("Enter a list of words: ").split()

longest_word(words)

print("The length of the longest word", longest_word(words))