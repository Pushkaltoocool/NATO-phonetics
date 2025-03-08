import pandas

letters_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

letters_dict = {row.letter:row.code for (index, row) in letters_dataframe.iterrows()}



def give_list():
    word = input("What is your word: ").upper()
    words_list = [letters_dict[letter] for letter in word]
    print(words_list)


try:
    give_list()
except:
    print("Please includes alphabets only")
    give_list()


