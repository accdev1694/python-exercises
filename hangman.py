import random
from clear import clear

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word = random.choice(["hollandia", "bobo", "chivita"])

blanks = []
missed = 6

for _ in range(len(word)):
    blanks.append("_")
# print(blanks)

while True:
    guess = input("Guess a letter:\n")
    clear()
    if guess in blanks:
        print("You have guessed that word already, try another")

    for index, letter in enumerate(word):
        if letter == guess:
            blanks[index] = guess

    print(blanks)
    if guess not in word:
        print(stages[missed])
        missed -= 1
        print(f"You have {missed} chances left")
    if not "_" in blanks:
        # print(blanks)
        print("You Have won!!!")
        break
    elif missed == 0:
        print(stages[missed])
        print("You Have lost!!!")
        break
