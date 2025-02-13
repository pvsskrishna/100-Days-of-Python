import random
from art import chance,logo
from words import words_list

print(logo)
chances = 4

'''choosing the random word'''
chosen_word = random.choice(words_list)
print(f"(This is the chosen word for testing purpose: {chosen_word})")

'''creating the blank spaces which is of length equal to word'''
blank_lines = ""
for empty_spaces in range(len(chosen_word)):
    blank_lines += "_"
print("Word to Guess" + blank_lines)

game_over = False
correct_letters = []

while not game_over:
    print(f"***************************** {chances}/ 4 lives left **************************")
    guess = input("Guess the letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    # tallying the guess letter with every letter present in chosen word
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)

        # if the same letter is occurred more than one time in iteration, concatenating that letter again from correct_letters.
        elif letter in correct_letters:
            display += letter

        else:
            # if the guess not in chosen_word replacing with "_"
            display += "_"

    print(f"Word to guess: {display}")

    if guess not in chosen_word or guess not in correct_letters:
        chances -= 1
        print(f"You guessed {guess}, that's not in the word, you loose a life.")

        if chances == 0:
            print(chance[0])

        if chances == 0:
            game_over = True
            print(f"***************************** IT WAS {chosen_word}! YOU LOOSE! **************************")

        elif chances == 1:
            print(chance[1])

        elif chances == 2:
            print(chance[2])

        elif chances == 3:
            print(chance[3])

        elif chances == 4:
            print(chance[4])

    if '_' not in display:
        game_over = True
        print(f"***************************** YOU WIN! **************************")

# last step validation
if display == chosen_word:
    print('Game over: You won the game')
else:
    print('Game over: Hanged Man dead')







