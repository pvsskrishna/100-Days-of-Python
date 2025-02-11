import random
from art import rock,paper,scissor

graphics = [0,1,2]
graphic_images = [rock,paper,scissor]

def compare_score(u_score, c_score):
    if u_score > c_score:
        print('You are in lead!')
    elif u_score < c_score:
        print("computer is leading")
    else:
        print('It is a tie!')

def round_winner(u_choice, c_choice):
    if u_choice == c_choice:
        print('Game is draw. Both the players will gain 1 score each')
        return 'draw'
    elif (u_choice == 0 and c_choice == 2) or \
            (u_choice == 1 and c_choice == 0) or \
            (u_choice == 2 and c_choice == 1):
        print('You win!')
        return 'user'
    else:
        print('You loose!')
        return 'computer'

def update_scores(result,u_score,c_score):
    if result == 'user':
        u_score += 1
    elif result == 'computer':
        c_score += 1
    else:
        c_score += 1
        u_score += 1
    return u_score,c_score

def target_score_check(t_score,u_score,c_score):
    if u_score >= t_score:
        print('Congratulations!, You won the game!!!')
        return True

    elif c_score >= t_score:
        print('Better luck next time, You loose!!!')
        return True

def rock_paper_scissor():
    user_score = 0
    computer_score = 0
    target_score = 10

    game_is_on = True
    while game_is_on:
        try:
            user_choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
            if user_choice not in [0,1,2]:
                print('Invalid input, Please enter a number between 0 and 2.')
                continue
        except ValueError:
            print('Invalid input, Please enter a number between 0 and 2.')
            continue

        print(f"User choice is: {user_choice} \n"
              f"User graphic: {graphic_images[user_choice]}")

        computer_choice = random.randint(0,2)
        print(f"computer choice is: {computer_choice} \n"
              f"Computer graphic: {graphic_images[computer_choice]}")

        result = round_winner(user_choice, computer_choice)
        user_score,computer_score = update_scores(result,user_score,computer_score)


        print(f"Your score is: {user_score} | Computer score is: {computer_score}")
        compare_score(user_score,computer_score)

        if target_score_check(target_score,user_score,computer_score):
            game_is_on = False

rock_paper_scissor()
play_again = input("Do you want to play again? Type 'y' if not 'n': ").lower()

if play_again == 'y':
    print('\n' * 20)
    rock_paper_scissor()
else:
    print(f'Thank You!')



