from Treasure_art import LOGO

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")

choice1 = input("You are at the crossroad. "
                "Which way do you want to go? 'Left' or 'Right': \n").lower()

if choice1 == 'left':
    choice2 = input("You come to the lake, "
                    "There is a Island in middle of the lake"
                    "What do you want to do? "
                    "Type 'wait' to wait for the boat or "
                    "Type 'Swim' to cross the lake: \n").lower()

    if choice2 == 'wait':
        choice3 = input("You have arrived the Island, "
                        "There is a house with 3 doors. "
                        "Which door you want to open? "
                        "'Yellow',or 'Red' or 'Blue': \n").lower()

        if choice3 == 'yellow':
            print('You found the treasure!!!')
            print(LOGO)
          
        elif choice3 == 'red':
            print('Burned by fire.Game Over.')
          
        elif choice3 == 'blue':
            print('Eaten by beasts.Game Over.')
          
        else:
            print("You choose the door that doesn't exist, Game Over")
          
    else:
        print('Attacked by trout-Game Over.')
      
else:
    print("Fall into a hole-Game Over.")


