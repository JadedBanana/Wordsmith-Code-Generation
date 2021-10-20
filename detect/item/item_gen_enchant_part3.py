"""
Generates all the item detection files for enchants (part 3 / making the item modification JSON for part 1).
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each entry in the list
for entry in word_list:
    # Iterate through each DEFINITION of each word
    for entry2 in word_list[entry]:
        # Cancel if it's manual or if it's not a item or it's not an enchant
        if 'manual' in entry2 or 'item' not in entry2 or 'enchant' not in entry2:
            continue

        # Practically hardcoded thing, json item modifiers are simple
        full = '{\n'
        full += '"function": "minecraft:set_enchantments",\n'
        full += '  "enchantments": {\n'
        full += '    "minecraft:' + entry2['item'] + '": -255\n'
        full += '  }\n'
        full += '}'
        
        # Write
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/item_modifiers/{}.json'.format(entry2['item'].replace(' ', '_').replace('\'', '_')))