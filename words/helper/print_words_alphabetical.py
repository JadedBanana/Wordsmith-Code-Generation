
from util import writer
from words.word_settings import word_file
import os
import json

word_list = word_file.words
word_letter_dict = {}

word_list = [word for word in word_list]
word_list.sort()
for word in word_list:
    print(word)
    if word[-1] not in word_letter_dict:
        word_letter_dict[word[-1]] = 0
    word_letter_dict[word[-1]] += 1

print(word_letter_dict)