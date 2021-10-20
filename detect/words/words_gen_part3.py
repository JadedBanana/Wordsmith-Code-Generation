"""
Generates all the word detection files (part 3 / checking if the word begins with the right letter).
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Set up letter numbers
letter_numbers = ' abcdefghijklmnopqrstuvwxyz'

# Iterate through each word in the word list
for entry in word_list:

    # Generate full string
    full = '# Check if word starts with required letter or required letter is 0'
    # If the first letter is a, we can do 0..1 instead of 2 different functions
    if entry[0] == 'a':
        full += '\nexecute unless score #required_letter vars matches 0..1 run function wordsmith:detect/punish_wrong_letter'
        full += '\nexecute if score #required_letter vars matches 0..1 run function wordsmith:detect/words/' + entry.replace(' ', '_').replace('\'', '_') + '4'
    # Otherwise, we have to do 2 different checks
    else:
        full += '\nexecute unless score #required_letter vars matches 0 unless score #required_letter vars matches {} run function wordsmith:detect/punish_wrong_letter'.format(letter_numbers.find(entry[0]))
        full += '\nexecute if score #required_letter vars matches 0 run function wordsmith:detect/words/' + entry.replace(' ', '_').replace('\'', '_') + '4'
        full += '\nexecute if score #required_letter vars matches {} run function wordsmith:detect/words/'.format(letter_numbers.find(entry[0])) + entry.replace(' ', '_').replace('\'', '_') + '4'

    # Write
    writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/words/{}3.mcfunction'.format(entry.replace(' ', '_').replace('\'', '_')))