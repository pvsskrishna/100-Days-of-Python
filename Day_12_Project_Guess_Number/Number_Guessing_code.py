from Programes.Days.Day_12_Project_Guess_Number.Number_Guessing_art import LOGO
import random
print(LOGO)
print("Welcome to the Number Guessing Game!")

def difficulty(level):
    """Based on Level choose, It wii provide the attempts to guess number"""
    #attempts = 0
    if level == "easy":
        attempts = 10
        print(f"you have {attempts} attempts to guess a number")
        return attempts
    elif level == "hard":
        attempts = 5
        print(f"you have {attempts} attempts to guess a number")
        return attempts
    elif level != "easy" or level != "hard":
        attempts = 10
        print(f"I can take that as you are choosing for easy level. So,you have {attempts} attempts to guess a number")
        return attempts

def checking_number(c_num,g_num):
    """Compares the Computer number and guessed number are matching or Too High or Too Low"""
    if c_num == g_num:
        return "Matching"
    elif g_num > c_num:
        return "Too High"
    elif g_num < c_num:
        return "Too Low"


def start_guessing():

    difficulty_level = input(f"Choose your difficulty. Type 'easy' or 'hard': ").lower()

    print("I'm thinking of a number from 1 to 100.")
    computer_number = random.randint(1, 100)
    #print(computer_number)

    chances = difficulty(difficulty_level)

    while chances > 0:
        guess_number = int(input("Make a guess: "))

        result = checking_number(computer_number, guess_number)
        if result == "Matching":
            print("Congratulations!!! Correct Guess.")
            chances = 0

        else:
            print(f"{result}")
            chances -= 1 #decreasing the chances by 1

            if chances == 0:
                print(f"you have {chances} attempts to guess a number, You Loose")
                print(f"The correct number is {computer_number}")

            else:
                print(f"you have {chances} attempts to guess a number")

start_guessing()

restart = True
while restart:
    ask = input(f"do you want to play again, Type 'yes' or 'no': ").lower()
    if ask == 'yes':
        print('\n'*20)
        start_guessing()
    elif ask == 'no':
        print("Thank you for playing")
        restart = False
    else:
        print("You entered the wrong input. So, Please rerun the program")
        restart = False














