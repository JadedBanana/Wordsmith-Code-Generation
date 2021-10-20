"""
Generates all the item detection files for potions (part 1 / deleting items).
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each entry in the list
for entry in word_list:
    # Iterate through each DEFINITION of each word
    for entry2 in word_list[entry]:
        # Cancel if it's manual or if it's not a block
        if 'manual' in entry2 or 'item' not in entry2 or 'enchant' in entry2 or 'potion' in entry2:
            continue

        # Generate full string
        # Summon the armor stands.
        full = '# Summon armor stands\n'
        full += 'scoreboard players operation #spreaded_armor_stands vars = #curr_item_spawning_density vars\n'
        full += 'function wordsmith:detect/spread_armor_stands_r1\n'
        # Finally get into the dropping part! Drop the items.
        full += '\n# Summon item\n'
        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + entry2['item'] + '",Count:1b}}\n'
        # And the particle effects...
        full += '\n# Give fancy particle for the current team\n'
        full += 'execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
        full += 'execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
        full += 'execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
        full += 'execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
        # Kill the armor stands
        full += '\n# Kill the armor stands\n'
        full += 'kill @e[type=minecraft:armor_stand,tag=spawner]'
        # Then do ALL OF THAT again, but a little higher.
        full += '\n\n# Do all of that again\n' + full.replace('~10', '~12')

        # Write
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}2.mcfunction'.format(entry2['item'].replace(' ', '_').replace('\'', '_')))