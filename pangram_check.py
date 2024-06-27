# import the string module
import string

# Exercise 14: Write a function to check if a given string is a pangram.
# A pangram is a sentence that has every letter of the alphabet repeated.

# define function with string as parameter:
def is_pangram(str):
    alphabets = list(string.ascii_lowercase)
    for char in alphabets:
        if char in str:
            print(True)

print(False)
            
is_pangram("The quick brown fox jumps over the lazy dog")
