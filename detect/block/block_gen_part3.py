"""
Generates all the block detection files (part 1 / deleting blocks for blocks with blanket terms that use them exclusively).
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
        if 'manual' in entry2 or 'block' not in entry2:
            continue

        # If there's a blanket term that only uses one block (this block), we split this function into THREE pieces rather than 2.
        blanket_one_block = False
        for entry3 in word_list:
            for entry4 in word_list[entry3]:
                if 'group' in entry4 and 'one_block' in entry4 and entry4['one_block'] == entry2['block']:
                    blanket_one_block = True

        if blanket_one_block:
            # Generate full string
            full = '# Attempt to fill / kill / clear in block\n'
            # If it can be an item, we kill its item form
            if not 'not_item' in entry2:
                full += 'execute store result score #blocks_killed1 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + entry2['block'] + '"}}]\n'
                # If it can be dropped from the sky, we clear it
                if not 'dont_drop' in entry2:
                    full += 'execute store result score #blocks_killed2 vars run kill @e[type=minecraft:falling_block,nbt={BlockState:{Name:"minecraft:' + entry2['block'] + '"}}]\n'
            # Again here, but with blocks_killed1 instead of 2
            elif not 'dont_drop' in entry2:
                full += 'execute store result score #blocks_killed1 vars run kill @e[type=minecraft:falling_block,nbt={BlockState:{Name:"minecraft:' + entry2['block'] + '"}}]\n'
            # Insert hardcoded deletion algoritm that fills throughout the world
            full += 'execute store result score #blocks_replaced1 vars run fill ~-22 0 ~-22 ~22 15 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced2 vars run fill ~-22 16 ~-22 ~22 31 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced3 vars run fill ~-22 32 ~-22 ~22 47 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced4 vars run fill ~-22 48 ~-22 ~22 63 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced5 vars run fill ~-22 64 ~-22 ~22 79 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced6 vars run fill ~-22 80 ~-22 ~22 95 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced7 vars run fill ~-22 96 ~-22 ~22 111 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced8 vars run fill ~-22 112 ~-22 ~22 127 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced9 vars run fill ~-22 128 ~-22 ~22 143 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced10 vars run fill ~-22 144 ~-22 ~22 159 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced11 vars run fill ~-22 160 ~-22 ~22 175 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced12 vars run fill ~-22 176 ~-22 ~22 191 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced13 vars run fill ~-22 192 ~-22 ~22 207 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced14 vars run fill ~-22 208 ~-22 ~22 223 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced15 vars run fill ~-22 224 ~-22 ~22 239 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            full += 'execute store result score #blocks_replaced16 vars run fill ~-22 240 ~-22 ~22 255 ~22 {} replace {}\n'.format('minecraft:water' if 'replace_with_water' in entry2 else 'minecraft:air', entry2['replacement_tag'] if 'replacement_tag' in entry2 else 'minecraft:' + entry2['block'])
            # Likewise, but a potted version
            if 'potted_version' in entry2:
                full += 'execute store result score #blocks_replaced17 vars run fill ~-22 0 ~-22 ~22 15 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced18 vars run fill ~-22 16 ~-22 ~22 31 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced19 vars run fill ~-22 32 ~-22 ~22 47 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced20 vars run fill ~-22 48 ~-22 ~22 63 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced21 vars run fill ~-22 64 ~-22 ~22 79 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced22 vars run fill ~-22 80 ~-22 ~22 95 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced23 vars run fill ~-22 96 ~-22 ~22 111 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced24 vars run fill ~-22 112 ~-22 ~22 127 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced25 vars run fill ~-22 128 ~-22 ~22 143 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced26 vars run fill ~-22 144 ~-22 ~22 159 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced27 vars run fill ~-22 160 ~-22 ~22 175 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced28 vars run fill ~-22 176 ~-22 ~22 191 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced29 vars run fill ~-22 192 ~-22 ~22 207 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced30 vars run fill ~-22 208 ~-22 ~22 223 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced31 vars run fill ~-22 224 ~-22 ~22 239 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
                full += 'execute store result score #blocks_replaced32 vars run fill ~-22 240 ~-22 ~22 255 ~22 flower_pot replace minecraft:potted_{}\n'.format(entry2['block'])
            # If it can be an item, we clear it from everyone
            if not 'not_item' in entry2:
                full += 'execute store result score #blocks_cleared vars run clear @a minecraft:{}'.format(entry2['block'])

            # Write
            writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/block/{}3.mcfunction'.format(entry2['block'].replace(' ', '_').replace('\'', '_')))