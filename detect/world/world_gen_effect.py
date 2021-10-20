"""
Generates all the world detection files for effects.
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each entry in the list
for entry in word_list:
    # Iterate through each DEFINITION of each word
    for entry2 in word_list[entry]:
        # Cancel if it's manual or if it's not a world entry or it's not an effect
        if 'manual' in entry2 or 'world' not in entry2 or 'effect' not in entry2:
            continue

        # Practically hardcoded thing, check if effect is active, clear if it is, and give to all if it isn't
        full = '# Detect entities with effect\n'
        full += 'execute store result score #effects_cleared vars run effect clear @e minecraft:' + entry2['world'] + '\n'
        full += '\n# If effect not cleared, give it to all players\n'
        full += 'execute if score #effects_cleared vars matches 0 run effect give @a[scores={deaths=0}] minecraft:' + entry2['world'].replace(' ', '_').replace('\'', '_') + ' 1000000 0'

        # Write.
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')))