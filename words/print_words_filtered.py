from words import words_en
import os

worddict = words_en.words

for word in worddict:
    for entry in worddict[word]:
        if 'group' in entry and 'overpowered' in entry:
                print(entry)