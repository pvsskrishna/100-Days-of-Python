import random
import string

def alpha_characters(nr_alphabets):
    """returns a list having random alphabets length equal to parameter(nr_alphabets) integer value"""
    alphabets = list(string.ascii_lowercase)
    random_alphabets = []
    for _ in range(nr_alphabets):
        random_alphabet = random.choice(alphabets)
        random_alphabets.append(random_alphabet)
    return random_alphabets

def num_characters(nr_numbers):
    """returns a list having random numbers length equal to parameter(nr_numbers) integer value"""
    numbers = list(string.digits)
    random_numbers = []
    for _ in range(nr_numbers):
        random_number = random.choice(numbers)
        random_numbers.append(random_number)
    return random_numbers

def spl_characters(nr_spl_chars):
    """returns a list having random special symbols length equal to parameter(nr_spl_chars) integer value"""
    spl_chars = list(string.punctuation)
    random_spl_chars = []
    for _ in range(nr_spl_chars):
        random_spl_char = random.choice(spl_chars)
        random_spl_chars.append(random_spl_char)
    return random_spl_chars

def generate_password(no_of_alpha, no_of_numb, no_of_spl_sym, password=''):
    """It will generate a password in a string formate"""
    password_characters = alpha_characters(no_of_alpha) + num_characters(no_of_numb) + spl_characters(no_of_spl_sym)
    random.shuffle(password_characters)
    password = ''.join(password_characters)
    return password

print("Welcome to the Password Generator!")


no_of_alphabets = int(input("How many alphabets would you like to have? : "))
no_of_numbers = int(input("How many numbers would you like to have? : "))
no_of_special_symbols = int(input("How many special characters would you like to have? : "))

print(f"Here is your password: {generate_password(no_of_alphabets,no_of_numbers,no_of_special_symbols)}")
#generate_password(no_of_alphabets,no_of_numbers,no_of_special_symbols)





