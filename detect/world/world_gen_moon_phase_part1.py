"""
Generates all the world detection files for moon phases (part 1 / the moon is on the desired phase right now)
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

        # Practically hardcoded thing, if the moon is on the right phase then add 4 days, otherwise run part 2
        full = '# Get the current day\n'
        full += 'execute store result score #day_query vars run time query day\n'
        full += 'scoreboard players set #temp vars 8\n'
        full += 'scoreboard players operation #day_query vars %= #temp vars\n'
        full += '\n# If current day matches desired phase, change\n'
        full += 'execute if score #day_query vars matches {} run time add 4d\n'.format(entry2['moon_phase'])
        full += '\n# Otherwise, set to desired phase\n'
        full += 'execute unless score #day_query vars matches {} run function wordsmith:detect/world/{}2'.format(entry2['moon_phase'], entry2['world'])

        # Write.
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')))