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

        # Practically hardcoded thing, attempt to get rid of items, and if you can't, schedule part 2
        full = '# Attempt to kill / clear item'
        full += '\nexecute store result score #items_killed vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + entry2['item'] + '"}}]'
        full += '\nexecute store result score #items_cleared vars run clear @a minecraft:' + entry2['item']
        full += '\n\n# If item not killed / cleared, summon some'
        full += '\nexecute if score #items_killed vars matches 0 if score #items_cleared vars matches 0 run schedule function wordsmith:detect/item/{}2 1t'.format(entry2['item'])

        # Write.
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}.mcfunction'.format(entry2['item'].replace(' ', '_').replace('\'', '_')))