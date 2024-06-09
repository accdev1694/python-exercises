print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("Welcome to Treasure Island. Your mission is to find the treasure")
play = input("Would you like to play? (Y/N): ").lower()
if play == "y":
          name = input("What is your name: ").title()
          direction = input(f"{name}, type 'l' to go left or 'r' to go right: ").lower()
          if direction == "l":
                    action = input(f"{name}, would you like to swim 's' or wait 'w'? ").lower()
                    if action == "w":
                              door = input(f"{name}, which door do you like to enter? 'r', 'y', 'b': ").lower()
                              if door == 'y':
                                        print(name, ", Congratulations!!!")
                                        print("You have won")
                              elif door == 'b':
                                        print(name, ", You have been eaten by beasts!!!")
                                        print("Game Over")
                                        exit()
                              elif door == 'r':
                                        print(name, ", You have burnt by fire!!!")
                                        print("Game Over")
                                        exit()
                              else:                                        
                                        print("Game Over")
                                        exit()


                    else:
                              print(name, ", You have fallen into a hole!!!")
                              print("Game Over")
                              exit()
                    
          else:
                    print(name, ", You have been attacked by a trout!!!")
                    print("Game Over")
                    exit()

