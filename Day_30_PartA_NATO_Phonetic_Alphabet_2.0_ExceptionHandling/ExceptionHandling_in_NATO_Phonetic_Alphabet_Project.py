# NATO Phonetic Alphabet Project (Day_26 Project Enhancement)
#Scenario: Since, The code asks for the user input
    # code expects only alphabetic characters
    # so, There is a chance that user might enter Alphanumeric, Numeric and special chars
#So, To Handle that situation we need to handle the exceptions

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.to_dict()

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

def generate_phonetic_word():
    word = input("Enter the word: ").upper()
    try:
    # To Create a dictionary of the phonetic code words from a word that the user inputs.
        output_dict = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only Alphabets from Letters Please!!!")
        generate_phonetic_word()
    else:
        print(output_dict)

generate_phonetic_word()