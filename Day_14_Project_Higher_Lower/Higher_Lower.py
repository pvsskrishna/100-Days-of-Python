from pickle import GLOBAL
from replit import clear

from Higher_Lower_art import logo,vs
from Higher_Lower_Dataset import data
import random


def choices():
    choice =  random.choice(data)
    return choice

def game():
    def check_followers_count(c, d):
        a_count = c['follower_count']
        b_count = d['follower_count']
        if a_count > b_count:
            return a_count
        elif a_count < b_count:
            return b_count

    def high_low():
        """prints the person name, occupation and location to compare"""
        print(logo)
        print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}")

        print(vs)

        print(f"Against B: {b['name']}, a {b['description']} from {b['country']}")

    b = choices()
    correct = True
    score = 0

    while correct:
        a = b

        """To make the 'B' value mismatch with 'A' value"""
        b = choices()
        while b == a:
            b=choices()

        high_low()

        choose = input("Who has more followers? Type 'A' or 'B': ").lower()

        if choose == 'a':
            choose = a
        elif choose == 'b':
            choose = b

        if choose['follower_count'] == check_followers_count(a,b):
            score += 1
            clear()
            a = choose
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            correct = False

game()




