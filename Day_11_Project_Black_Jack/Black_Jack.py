import random
from Black_jack_art import logo

def deal_card():
    """Randomly provide a card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # it is a Blackjack score

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(u_score, c_score):
    """it will compare the user score and computer scores"""
    if u_score == c_score:
        return "Draw 🐼"
    elif c_score == 0:
        return "Loss, opponent has Blackjack😭"
    elif u_score == 0:
        return "Win with Blackjack 😁"
    elif c_score > 21:
        return "Opponent went over, you win 😉"
    elif u_score > 21:
        return "You went over, you loss 😢"
    elif u_score > c_score:
        return "You win 😀"
    else:
        return "You lose 😒"

def play_game():

    print(logo)
    computer_cards = []
    user_cards = []
    is_game_over = False
    user_score = -1
    computer_score = -1

    """ we are using -1 because 0 is equals to Blackjack. 
    so, to avoid that we are providing same score of -1 to both user and computer"""

    for _ in range(2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"user cards:{user_cards} and current score:{user_score}")
        print(f"computer 1st card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to take another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print('\n' * 1)
    print(f"user final hand {user_cards}, user final score: {user_score}")
    print(f"computer final hand {computer_cards}, computer final score: {computer_score}")
    print(compare_score(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' else 'n': ") == 'y':
    print('\n'* 20)
    play_game()

