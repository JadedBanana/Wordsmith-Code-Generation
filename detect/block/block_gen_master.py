"""
Generates all the block detection files (part 3 / being the manager of the other 2 block functions).
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

        # Generate full string
        # Next, we get into the part where we call the next function
        full = '# Attempt to clear blocks\n'
        full += 'function wordsmith:detect/block/clear/{}\n\n'.format(entry2['block'])
        full += '# If block not replaced, summon some\n'
        # Set the spawning density
        if 'drop_as_item' in entry2:
            full += 'scoreboard players operation #curr_item_spawning_density vars = #item_spawning_density vars\n'
        else:
            full += 'scoreboard players operation #curr_block_spawning_density vars = #block_spawning_density vars\n'
        # Do the same as the thing above to get the amount of blocks_killed variables
        if 'potted_version' in entry2:
            potted_checks = 'if score #blocks_replaced17 vars matches 0 if score #blocks_replaced18 vars matches 0 if score #blocks_replaced19 vars matches 0 if score #blocks_replaced20 vars matches 0 if score #blocks_replaced21 vars matches 0 if score #blocks_replaced22 vars matches 0 if score #blocks_replaced23 vars matches 0 if score #blocks_replaced24 vars matches 0 if score #blocks_replaced25 vars matches 0 if score #blocks_replaced26 vars matches 0 if score #blocks_replaced27 vars matches 0 if score #blocks_replaced28 vars matches 0 if score #blocks_replaced29 vars matches 0 if score #blocks_replaced30 vars matches 0 if score #blocks_replaced31 vars matches 0 if score #blocks_replaced32 vars matches 0 '
        else:
            potted_checks = ''
        if 'not_item' in entry2:
            if 'dont_drop' in entry2:
                full += 'execute if score #blocks_replaced1 vars matches 0 if score #blocks_replaced2 vars matches 0 if score #blocks_replaced3 vars matches 0 if score #blocks_replaced4 vars matches 0 if score #blocks_replaced5 vars matches 0 if score #blocks_replaced6 vars matches 0 if score #blocks_replaced7 vars matches 0 if score #blocks_replaced8 vars matches 0 if score #blocks_replaced9 vars matches 0 if score #blocks_replaced10 vars matches 0 if score #blocks_replaced11 vars matches 0 if score #blocks_replaced12 vars matches 0 if score #blocks_replaced13 vars matches 0 if score #blocks_replaced14 vars matches 0 if score #blocks_replaced15 vars matches 0 if score #blocks_replaced16 vars matches 0 {}run schedule function wordsmith:detect/block/drop/{} 1t'.format(potted_checks, entry2['block'].replace(' ', '_').replace('\'', '_'))
            else:
                full += 'execute if score #blocks_killed1 vars matches 0 if score #blocks_replaced1 vars matches 0 if score #blocks_replaced2 vars matches 0 if score #blocks_replaced3 vars matches 0 if score #blocks_replaced4 vars matches 0 if score #blocks_replaced5 vars matches 0 if score #blocks_replaced6 vars matches 0 if score #blocks_replaced7 vars matches 0 if score #blocks_replaced8 vars matches 0 if score #blocks_replaced9 vars matches 0 if score #blocks_replaced10 vars matches 0 if score #blocks_replaced11 vars matches 0 if score #blocks_replaced12 vars matches 0 if score #blocks_replaced13 vars matches 0 if score #blocks_replaced14 vars matches 0 if score #blocks_replaced15 vars matches 0 if score #blocks_replaced16 vars matches 0 {}run schedule function wordsmith:detect/block/drop/{} 1t'.format(potted_checks, entry2['block'].replace(' ', '_').replace('\'', '_'))
        elif 'dont_drop' in entry2:
            full += 'execute if score #blocks_killed1 vars matches 0 if score #blocks_replaced1 vars matches 0 if score #blocks_replaced2 vars matches 0 if score #blocks_replaced3 vars matches 0 if score #blocks_replaced4 vars matches 0 if score #blocks_replaced5 vars matches 0 if score #blocks_replaced6 vars matches 0 if score #blocks_replaced7 vars matches 0 if score #blocks_replaced8 vars matches 0 if score #blocks_replaced9 vars matches 0 if score #blocks_replaced10 vars matches 0 if score #blocks_replaced11 vars matches 0 if score #blocks_replaced12 vars matches 0 if score #blocks_replaced13 vars matches 0 if score #blocks_replaced14 vars matches 0 if score #blocks_replaced15 vars matches 0 if score #blocks_replaced16 vars matches 0 {}if score #blocks_cleared vars matches 0 run schedule function wordsmith:detect/block/drop/{} 1t'.format(potted_checks, entry2['block'].replace(' ', '_').replace('\'', '_'))
        else:
            full += 'execute if score #blocks_killed1 vars matches 0 if score #blocks_killed2 vars matches 0 if score #blocks_replaced1 vars matches 0 if score #blocks_replaced2 vars matches 0 if score #blocks_replaced3 vars matches 0 if score #blocks_replaced4 vars matches 0 if score #blocks_replaced5 vars matches 0 if score #blocks_replaced6 vars matches 0 if score #blocks_replaced7 vars matches 0 if score #blocks_replaced8 vars matches 0 if score #blocks_replaced9 vars matches 0 if score #blocks_replaced10 vars matches 0 if score #blocks_replaced11 vars matches 0 if score #blocks_replaced12 vars matches 0 if score #blocks_replaced13 vars matches 0 if score #blocks_replaced14 vars matches 0 if score #blocks_replaced15 vars matches 0 if score #blocks_replaced16 vars matches 0 {}if score #blocks_cleared vars matches 0 run schedule function wordsmith:detect/block/drop/{} 1t'.format(potted_checks, entry2['block'].replace(' ', '_').replace('\'', '_'))

        # Write
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/block/master/{}.mcfunction'.format(entry2['block'].replace(' ', '_').replace('\'', '_')))