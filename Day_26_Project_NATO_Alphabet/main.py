#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.to_dict()
#print(data_dict)

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter the word: ").upper()
#letters = [letter for letter in player_input]

# To Create a dictionary of the phonetic code words from a word that the user inputs.
# If we want in dictionary
output_dict = {f"{letter} for":phonetic_dict[letter] for letter in word}
print(output_dict)

# To Create a list of the phonetic code words from a word that the user inputs.
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
