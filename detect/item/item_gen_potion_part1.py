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
        # Cancel if it's manual or if it's not a item or it's not a potion
        if 'manual' in entry2 or 'item' not in entry2 or 'potion' not in entry2:
            continue

        # Detect potion type
        # Lingering
        if entry2['item'].endswith('_lingering_pot'):
            item_type = 'lingering_potion'
            potion_type = entry2['item'][:-14]
        # Splash
        elif entry2['item'].endswith('_splash_pot'):
            item_type = 'splash_potion'
            potion_type = entry2['item'][:-11]
        # Sippy
        else:
            item_type = 'potion'
            potion_type = entry2['item'][:-4]

        # Generate full string
        full = '# Attempt to kill / clear item'
        # Detect all the items on the ground
        # We also have to detect long + strong variations of each potion, so that's why this part is so long
        full += '\nexecute store result score #potions_killed1 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:' + potion_type + '"}}}]'
        if 'long' in entry2:
            full += '\nexecute store result score #potions_killed2 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:long_' + potion_type + '"}}}]'
            if 'strong' in entry2:
                full += '\nexecute store result score #potions_killed3 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:strong_' + potion_type + '"}}}]'
        elif 'strong' in entry2:
            full += '\nexecute store result score #potions_killed2 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:strong_' + potion_type + '"}}}]'
        # For splash potions, we also detect if a mid-air potion exists and kill it
        if item_type == 'splash_potion':
            full += '\nexecute store result score #potions_killed4 vars run kill @e[type=minecraft:potion,nbt={Item:{tag:{Potion:"minecraft:' + potion_type + '"}}}]'
        # Detect all the items in peoples' inventories
        # We also have to detect long + strong variations of each potion, so that's why this part is so long
        full += '\nexecute store result score #potions_cleared1 vars run clear @a minecraft:' + item_type + '{Potion:"minecraft:' + potion_type + '"}'
        if 'long' in entry2:
            full += '\nexecute store result score #potions_cleared2 vars run clear @a minecraft:' + item_type + '{Potion:"minecraft:long_' + potion_type + '"}'
            if 'strong' in entry2:
                full += '\nexecute store result score #potions_cleared3 vars run clear @a minecraft:' + item_type + '{Potion:"minecraft:strong_' + potion_type + '"}'
        elif 'strong' in entry2:
            full += '\nexecute store result score #potions_cleared2 vars run clear @a minecraft:' + item_type + '{Potion:"minecraft:strong_' + potion_type + '"}'
        # Then move on to the part where we call part 2
        full += '\n\n# If item not killed / cleared, summon some'
        # Set the spawning density
        full += '\nscoreboard players operation #curr_item_spawning_density vars = #item_spawning_density vars'
        # Create the detection method
        full += '\nexecute if score #potions_killed1 vars matches 0 '
        # We also have to detect long + strong variations of each potion, so that's why this part is so long
        if 'long' in entry2:
            if 'strong' in entry2:
                full += 'if score #potions_killed2 vars matches 0 if score #potions_killed3 vars matches 0' + (' if score #potions_killed4 vars matches 0' if item_type == 'splash_potion' else '') + ' if score #potions_cleared1 vars matches 0 if score #potions_cleared2 vars matches 0 if score #potions_cleared3 vars matches 0 run schedule function wordsmith:detect/item/{}2 1t'.format(entry2['item'])
            else:
                full += 'if score #potions_killed2 vars matches 0' + (' if score #potions_killed4 vars matches 0' if item_type == 'splash_potion' else '') + ' if score #potions_cleared1 vars matches 0 if score #potions_cleared2 vars matches 0 run schedule function wordsmith:detect/item/{}2 1t'.format(entry2['item'])
        elif 'strong' in entry2:
            full += 'if score #potions_killed2 vars matches 0' + (' if score #potions_killed4 vars matches 0' if item_type == 'splash_potion' else '') + ' if score #potions_cleared1 vars matches 0 if score #potions_cleared2 vars matches 0 run schedule function wordsmith:detect/item/{}2 1t'.format(entry2['item'])
        else:
            full += ('if score #potions_killed4 vars matches 0 ' if item_type == 'splash_potion' else '') + 'if score #potions_cleared1 vars matches 0 run schedule function wordsmith:detect/item/{}2 1t'.format(entry2['item'])

        # Write
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}.mcfunction'.format(entry2['item'].replace(' ', '_').replace('\'', '_')))