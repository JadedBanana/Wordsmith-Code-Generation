"""
Generates all the world detection files for gamerules.
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each entry in the list
for entry in word_list:
    # Iterate through each DEFINITION of each word
    for entry2 in word_list[entry]:
        # Cancel if it's manual or if it's not a world entry or it's not a gamerule
        if 'manual' in entry2 or 'world' not in entry2 or 'gamerule' not in entry2:
            continue

        # Practically hardcoded thing, invert gamerule status
        full = '# See if gamerule enabled\n'
        full += 'execute store result score #gamerule_enabled vars run gamerule ' + entry2['gamerule'] + '\n'
        full += '\n# Toggle gamerule\n'
        full += 'execute if score #gamerule_enabled vars matches 0 run gamerule ' + entry2['gamerule'] + ' true\n'
        full += 'execute if score #gamerule_enabled vars matches 1 run gamerule ' + entry2['gamerule'] + ' false'

        # Write.
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')))