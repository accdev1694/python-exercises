# Exercise 01: 

# Write a function to count the occurrences of each character 
# in a string and return them as a dictionary.

# define the function and initialize the dictionary and count
def count_occurence(string):
    occurences = {}
    count = 0
    
 # iterate through the string and add characters to the disctionary
    for char in string:
        if not char in occurences:
            occurences[char] = 1
            
 # increment count of multiple occurence of already added characters
        else:
            occurences[char] += 1

# create a formatted string of each character: count on a seperate line
    occurences = "\n".join([f"{char}: {count}" for char, count in occurences.items()])
    return occurences

print(count_occurence("the sun is going down too early today"))