# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(alphabet_df)
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}
# print(alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# program_finished = False
# while not program_finished:
#     user_input = input("Enter a word: ").upper()
#     try:
#         output = [alphabet_dict[letter] for letter in user_input]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         print(output)
#         program_finished = True


def phoneticize():
    user_input = input("Enter a word: ").upper()
    try:
        output = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        phoneticize()
    else:
        print(output)


phoneticize()
