from clear import clear
question_options = (
    ("What is the shape of the earth? (A, B, or C):\n"),
    ("How many continents are there in the world? (A, B, or C):\n"),
    ("Which of these is a source of protein? (A, B, or C):\n"),
    ("What does RAM stand for? (A, B, or C):\n")
)

answer_choices = [(
    ("A. Round"),
    ("B. Square"),
    ("C. Sphere")
),
    (
    ("A. 1"),
    ("B. 12"),
    ("C. 7")
),
    (
    ("A. Yams"),
    ("B. Beans"),
    ("C. Carrots")
),
    (
    ("A. Random Access Memory"),
    ("B. Rice and Meat"),
    ("C. Repeat and Memorize")
),
]

correct_answers = (
    ("C"),
    ("C"),
    ("B"),
    ("A")
)

clear()
right = 0
wrong = 3


for index, question in enumerate(question_options):
    while True:
        print(f"{index + 1}.) {question}")
        for choices in answer_choices[index]:
            print(choices)
        print()
        response = input().upper()
        clear()

        if response == correct_answers[index]:
            right += 1
            print(right)
            print("** Correct! **")
            print("--------")
            print()
            break

        else:
            if wrong >= 1:
                print("^^ Wrong ^^")
                print(f"You have {wrong} more tries...")
                wrong -= 1
                continue
            else:
                print("The Correct answer is", correct_answers[index])
                break

    wrong = 3


clear()
print(f"You Scored {int((right / len(question_options)) * 100)}%")
