"""
Generates all the block detection files (part 1 / deleting entities).
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each entry in the list
for entry in word_list:
    # Iterate through each DEFINITION of each word
    for entry2 in word_list[entry]:
        # Cancel if it's manual or if it's not a entity
        if 'manual' in entry2 or 'entity' not in entry2:
            continue

        # Practically hardcoded thing, attempt to teleport all matching entities into the void and on failure run part 2
        full = '# Attempt to kill mob\n'
        full += 'execute store result score #entities_killed vars run tp @e[type=minecraft:' + entry2['entity'] + ',distance=..300] ~ -500 ~\n'
        full += '\n# If mob not killed, summon some\n'
        full += 'scoreboard players operation #curr_entity_spawning_density vars = #entity_spawning_density vars\n'
        full += 'execute if score #entities_killed vars matches 0 run schedule function wordsmith:detect/entity/' + entry2['entity'] + '2 1t'

        # Write
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/entity/{}.mcfunction'.format(entry2['entity'].replace(' ', '_').replace('\'', '_')))