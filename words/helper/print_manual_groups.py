import os
from words.word_settings import word_file

# Setup word list
word_list = word_file.words


def remove_numbers(word):
    for i in '0123456789':
        word = word.strip(i)
    return word

for word in word_list:
    for entry in word_list[word]:
        if 'group' in entry and 'manual' in entry:
            print(entry)