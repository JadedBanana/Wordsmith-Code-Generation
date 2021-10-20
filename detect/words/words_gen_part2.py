"""
Generates all the word detection files (part 2 / checking if word has been used).
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each word in the word list
for entry in word_list:

    # Practically hardcoded thing, check if the word has been previously used
    full = '# Check if word used\n'
    full += 'execute if score #{} used matches 1 run function wordsmith:detect/punish_used\n'.format(entry.replace(' ', '_').replace('\'', '_'))
    full += 'execute unless score #{} used matches 1 run function wordsmith:detect/words/'.format(entry.replace(' ', '_').replace('\'', '_')) + entry.replace(' ', '_').replace('\'', '_') + '3'

    # Write
    writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/words/{}2.mcfunction'.format(entry.replace(' ', '_').replace('\'', '_')))