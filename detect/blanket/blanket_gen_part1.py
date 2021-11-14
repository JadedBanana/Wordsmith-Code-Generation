"""
Generates all the blanket detection files.
If any of the blanket term's parts are not implemented, it won't write; otherwise, it will.
"""
from util import writer, path
from words.word_settings import word_file
import os

# Setup word list
word_list = word_file.words

# Iterate through each entry in the list
for entry in word_list:
    # Iterate through each DEFINITION of each word
    for entry2 in word_list[entry]:
        # Cancel if it's manual or if it's not a blanket term
        if 'manual' in entry2 or 'group' not in entry2:
            continue
        blanket_name_no_nums = entry2['group']
        for i in '0123456789':
            blanket_name_no_nums = blanket_name_no_nums.strip(i)

        # Establish 2 things here, so each part can do its own thing.
        first_half = ''
        function_line = 'execute '

        # Block part
        if 'block' in entry2['prereq']:
            first_half += '# Block part\n'
            # One_block
            if 'one_block' in entry2:
                if not path.isfile('datapacks/Wordsmith/data/wordsmith/functions/detect/block/{}3.mcfunction'.format(entry2['one_block'])):
                    continue
                first_half+= 'function wordsmith:detect/block/{}3\n\n'.format(entry2['one_block'])
                function_line += 'if score #blocks_killed1 vars matches 0 if score #blocks_killed2 vars matches 0 if score #blocks_replaced1 vars matches 0 if score #blocks_replaced2 vars matches 0 if score #blocks_replaced3 vars matches 0 if score #blocks_replaced4 vars matches 0 if score #blocks_replaced5 vars matches 0 if score #blocks_replaced6 vars matches 0 if score #blocks_replaced7 vars matches 0 if score #blocks_replaced8 vars matches 0 if score #blocks_replaced9 vars matches 0 if score #blocks_replaced10 vars matches 0 if score #blocks_replaced11 vars matches 0 if score #blocks_replaced12 vars matches 0 if score #blocks_replaced13 vars matches 0 if score #blocks_replaced14 vars matches 0 if score #blocks_replaced15 vars matches 0 if score #blocks_replaced16 vars matches 0 if score #blocks_cleared vars matches 0 '
            # More than one block
            else:
                if not path.isfile('datapacks/Wordsmith/data/wordsmith/functions/detect/blanket/block/{}.mcfunction'.format(blanket_name_no_nums)):
                    continue
                first_half+= 'function wordsmith:detect/blanket/block/{}\n\n'.format(blanket_name_no_nums)
                function_line += 'if score #group_blocks_deleted vars matches 0 '

        # Item part
        if 'item' in entry2['prereq']:
            first_half += '# Item part\n'
            # One_block
            if 'one_item' in entry2:
                if not path.isfile('datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}3.mcfunction'.format(entry2['one_item'])):
                    continue
                first_half+= 'function wordsmith:detect/item/{}3\n\n'.format(entry2['one_item'])
            # More than one block
            else:
                if not path.isfile('datapacks/Wordsmith/data/wordsmith/functions/detect/blanket/item/{}.mcfunction'.format(blanket_name_no_nums)):
                    continue
                first_half+= 'function wordsmith:detect/blanket/item/{}\n\n'.format(blanket_name_no_nums)

        # Entity part
        if 'entity' in entry2['prereq']:
            continue

        # World part
        if 'world' in entry2['prereq']:
            continue

        # If the drop_as part is a tuple, we know we only drop one thing, so we can do that part here.
        if 'drop_as' not in entry2:
            continue
        if type(entry2['drop_as']) is tuple:
            function_line = 'scoreboard players operation #curr_{}_spawning_density vars = #{}_spawning_density vars\n'.format(entry2['drop_as'][0], entry2['drop_as'][0]) + function_line
            function_line += 'run schedule function wordsmith:detect/{}/{}2 1t'.format(entry2['drop_as'][0], entry2['drop_as'][1])
        else:
            function_line += 'run schedule function wordsmith:detect/block/{}_2 1t'.format(entry2['group'])

        # Modify the start of the function_line to have a comment.
        function_line = '# If block not replaced, summon some\n' + function_line

        # Write.
        writer.write(first_half + function_line, 'datapacks/Wordsmith/data/wordsmith/functions/detect/blanket/{}.mcfunction'.format(entry2['group']))

