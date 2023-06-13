import pandas


nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

# print(nato_alphabet)

nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

print(nato_dict)

code_word = input('Enter Code word: ').upper()
# As individuals
# for letter in code_word:
#     print(nato_dict[letter])
# As a list
output = [nato_dict[letter] for letter in code_word]
print(output)