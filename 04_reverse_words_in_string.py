# Exercise 04:
# Write a function to reverse the words in a string

# define the function with string parameter
def reverse_words(string):
# split string at point of spaces and assign to new vvariable
    splitted_string = string.split(" ")
# reverse the order of the words join the spaces back with spaces
    result = " ".join(splitted_string[::-1])
    return result
print(reverse_words("oloche aboje emmanuel"))