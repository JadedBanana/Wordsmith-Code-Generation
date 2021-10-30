
from util import writer
from words.word_settings import word_file
import os
import json

word_list = word_file.words

# Definition of recursive method
def get_recursive_blocklist(blocks):
    blocks2 = blocks
    for block in blocks:
        if '#' in block:
            if block.startswith('#wordsmith:'):
                tag_list3 = json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/tags/blocks', block[11:] + '.json'), 'r'))
                for block2 in get_recursive_blocklist(tag_list3['values']):
                    if block2 not in blocks2:
                        blocks2.append(block2)
            else:
                print('HASHTAG IN GROUP ' + group + ' WITH NO LINKAGE')
                exit(-1)
            blocks2.remove(block)
    return blocks2

# Definition of recursive method 2
def get_recursive_itemlist(items):
    items2 = items
    for item in items:
        if '#' in item:
            if item.startswith('#wordsmith:'):
                tag_list3 = json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/tags/items', item[11:] + '.json'), 'r'))
                for item2 in get_recursive_itemlist(tag_list3['values']):
                    if item2 not in items2:
                        items2.append(item2)
            else:
                print('HASHTAG IN GROUP ' + group + ' WITH NO LINKAGE')
                exit(-1)
            items2.remove(item)
    return items2

# Get list of groups
word_list2 = []
for entry in word_list:
    for entry2 in word_list[entry]:
        if 'manual' in entry2:
            continue
        if 'group' in entry2:
            name = entry2['group']
            for i in '0123456789':
                name = name.strip(i)
            if name not in word_list2:
                word_list2.append(entry2['group'])

# Of groups, check for block tags and item tags
tag_list_block = os.listdir('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/tags/blocks')
tag_list_item = os.listdir('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/tags/items')
for group in word_list2:
    if group + '.json' in tag_list_block and group + '_blocklist.json' in tag_list_item:
        try:
            tag_list_block2 = json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/tags/blocks', group + '.json'), 'r'))
            tag_list_item2 = json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/tags/items', group + '_blocklist.json'), 'r'))
        except json.decoder.JSONDecodeError as e:
            print(group)
            print(e)
            exit(-1)

        blocks = get_recursive_blocklist(tag_list_block2['values'])
        items = get_recursive_blocklist(tag_list_item2['values'])

        function = '# Kill commands\n'
        for i in range(len(blocks)):
            function += 'execute store result score #blocks_killed' + str(2*i+1) + ' vars run kill @e[type=minecraft:item,nbt={Item:{id:"' + blocks[i] + '"}}]\n'
            function += 'execute store result score #blocks_killed' + str(2*i+2) + ' vars run kill @e[type=minecraft:falling_block,nbt={BlockState:{Name:"' + blocks[i] + '"}}]\n'
        function += '\n# Fill commands\n'
        function += 'execute store result score #blocks_replaced1 vars run fill ~-22 0 ~-22 ~22 15 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced2 vars run fill ~-22 16 ~-22 ~22 31 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced3 vars run fill ~-22 32 ~-22 ~22 47 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced4 vars run fill ~-22 48 ~-22 ~22 63 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced5 vars run fill ~-22 64 ~-22 ~22 79 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced6 vars run fill ~-22 80 ~-22 ~22 95 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced7 vars run fill ~-22 96 ~-22 ~22 111 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced8 vars run fill ~-22 112 ~-22 ~22 127 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced9 vars run fill ~-22 128 ~-22 ~22 143 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced10 vars run fill ~-22 144 ~-22 ~22 159 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced11 vars run fill ~-22 160 ~-22 ~22 175 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced12 vars run fill ~-22 176 ~-22 ~22 191 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced13 vars run fill ~-22 192 ~-22 ~22 207 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced14 vars run fill ~-22 208 ~-22 ~22 223 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced15 vars run fill ~-22 224 ~-22 ~22 239 ~22 air replace #wordsmith:' + group + '\n'
        function += 'execute store result score #blocks_replaced16 vars run fill ~-22 240 ~-22 ~22 255 ~22 air replace #wordsmith:' + group + '\n'
        function += '\n# Clear command\n'
        function += 'execute store result score #blocks_cleared vars run clear @a[scores={deaths=0}] #wordsmith:' + group + '_blocklist\n'
        function += '\n# Set scoreboard value of whether or not blocks were deleted\n'
        function += 'scoreboard players set #group_blocks_deleted vars 1\n'
        function += 'execute '
        for i in range(len(blocks)):
            function += 'if score # blocks_killed{} vars matches 0 '.format(2*i+1)
            function += 'if score # blocks_killed{} vars matches 0 '.format(2*i+2)
        function += 'if score #blocks_replaced1 vars matches 0 if score #blocks_replaced2 vars matches 0 if score #blocks_replaced3 vars matches 0 if score #blocks_replaced4 vars matches 0 if score #blocks_replaced5 vars matches 0 if score #blocks_replaced6 vars matches 0 if score #blocks_replaced7 vars matches 0 if score #blocks_replaced8 vars matches 0 if score #blocks_replaced9 vars matches 0 if score #blocks_replaced10 vars matches 0 if score #blocks_replaced11 vars matches 0 if score #blocks_replaced12 vars matches 0 if score #blocks_replaced13 vars matches 0 if score #blocks_replaced14 vars matches 0 if score #blocks_replaced15 vars matches 0 if score #blocks_replaced16 vars matches 0 if score #blocks_cleared vars matches 0 run scoreboard players set #group_blocks_deleted vars 0'

        writer.write(function, 'datapacks/Wordsmith/data/wordsmith/functions/detect/blanket/block/{}.mcfunction'.format(group))