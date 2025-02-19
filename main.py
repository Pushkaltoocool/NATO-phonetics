import pandas

letters_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

letters_dict = {row.letter:row.code for (index, row) in letters_dataframe.iterrows()}

word = input("What is your word: ").upper()

words_list = [letters_dict[letter] for letter in word]
print(words_list)