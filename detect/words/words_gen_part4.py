"""
Generates all the word detection files (part 4 / checking if the word leads to a dead end).
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each word in the word list
for entry in word_list:

    # Practically hardcoded thing, check if the word leads to a dead end
    full = '# Check if word leads to a dead end'
    full += '\nexecute if score #{}_words used = #{}_words_max vars run function wordsmith:detect/punish_dead_end'.format(entry[-1], entry[-1])
    full += '\nexecute unless score #{}_words used = #{}_words_max vars run function wordsmith:detect/words/'.format(entry[-1], entry[-1]) + entry.replace(' ', '_').replace('\'', '_') + '5'

    # Write
    writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/words/{}4.mcfunction'.format(entry.replace(' ', '_').replace('\'', '_')))