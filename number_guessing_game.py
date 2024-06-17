import random
from clear import clear


while True:
    top_range = input("What's your max range\n")
    if not top_range.isdigit():
        print("Type an actual number")
    else:
        top_range = int(top_range)
        break

random_number = random.randint(0, top_range)
counter = 0
while True:
    guess = input("Guess a number\n")
    clear()
    
    if not guess.isdigit():
        print("Type an actual number")
    else:        
        pass
    
    guess = int(guess)
    
    if 0 > guess > top_range:
        print("Guess must be within 0 and", top_range)
    elif guess < random_number:
        counter += 1
        print("Guess Higher")
    elif guess > random_number:
        counter += 1
        print("Guess Lower")
    else:
        break
    
print("You got it right after", counter, "tries")    