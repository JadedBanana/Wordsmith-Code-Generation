"""
Generates all the world detection files for moon phases (part 2 / CHANGE THE FUCKING MOON BABEY)
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each entry in the list
for entry in word_list:
    # Iterate through each DEFINITION of each word
    for entry2 in word_list[entry]:
        # Cancel if it's manual or if it's not a world entry or it's not a moon phase
        if 'manual' in entry2 or 'world' not in entry2 or 'moon_phase' not in entry2:
            continue

        # Generate full string
        full = '# Add time to the next moon phase'
        # For every day it could be, add a certain amount of days to make it the desired one
        for i in range(1, 8):
            full += '\nexecute if score #day_query vars matches {} run time add {}d'.format((entry2['moon_phase'] - i) % 8, i)

        # Write.
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}2.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')))