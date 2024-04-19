# Exercise 02:

# Write a function to remove all punctuation characters from a string.

# we define a function taking a string as parameter:

def remove_punctuations(string):
# create a new empty string to store alpha-numeric characters
    new_string = ""
# iterate through string and add alpha-numeric characters to new_string
    for char in string:
        if char.isalnum():
            new_string += char
    return new_string
            


print(remove_punctuations("hello, world!"))




