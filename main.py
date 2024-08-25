import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:
alphabet = {}
for indx, row in df.iterrows():
    letter = row['letter']
    code = row['code']
    alphabet[letter] = code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input('Enter a word: ')

to_list = [alphabet[letter.upper()] for letter in user if letter.upper() in alphabet]
print(to_list)