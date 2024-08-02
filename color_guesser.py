import random

computer = ['R', 'Y', 'G', 'B', 'W']
random.shuffle(computer)

counter = 0
correct_index = 0
correct_color = 0

while counter < 10:
    if correct_index == 5:
        break
    else:

        guess = list(input("Pick 5 colors by their first letters (no spaces):\n").upper())
        if len(guess) == 5:
            for index, letter in enumerate(guess):
                if letter in computer:
                    correct_color += 1
                    print(correct_color, 'color')
                    print(f"--- letter {letter} was found ---")
                else:
                    print(f"^^^ letter {letter} not found ^^^")
                    print()

                if guess[index] == computer[index]:
                    correct_index += 1
                    print(correct_index, 'index')
                    print(f"*** color {letter} at index {index} was right! ***")

            print("-----------------------------------------------------------------------------")
            counter += 1
            print(f"Correct colors: {correct_color} || Correct color Indexes: {correct_index}")
            print(f"You have {10 - counter} tries more")
            print("-----------------------------------------------------------------------------")
            print()
            correct_index = 0
            correct_color = 0

        else:
            print("Too many colors")

print()
print("-----------------------------------------------------------------------------")
print("Game Over")
print(f"Correct colors: {correct_color} || Correct color Indexes: {correct_index}")
print(f"It took you {counter} tries")
print("-----------------------------------------------------------------------------")
print()


