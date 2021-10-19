import json
import os

m = {
    'diamond_block': 'diamond block'
}

n = 7

letter_nums = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
}

for block_name in m:

    letter_end = block_name[-1]
    letter_start_num = letter_nums[block_name[0].lower()]
    block_formal_name = m[block_name].lower()
    block_formal_name_score = block_name.replace(' ', '_')
    letter_end_num = letter_nums[block_formal_name[-1]]

    if not os.path.isfile('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks/{}.mcfunction'.format(block_name)):
        continue

    block5 = '# Call punish_used function, if used\n'
    block5 += 'execute if score #{} used matches 1 run function wordsmith:detect/punish_used\n'.format(block_formal_name_score)
    block5 += '\n# Call punish_wrong_letter function, if wrong letter and not used\n'
    if letter_start_num == 1:
        block5 += 'execute unless score #{} used matches 1 unless score #required_letter vars matches 0..1 run function wordsmith:detect/punish_wrong_letter\n'.format(block_formal_name_score)
    else:
        block5 += 'execute unless score #{} used matches 1 unless score #required_letter vars matches 0 unless score #required_letter vars matches {} run function wordsmith:detect/punish_wrong_letter\n'.format(block_formal_name_score, letter_start_num)
    block5 += '\n# Call punish_dead_end function, if word would lead to a dead end\n'
    if letter_start_num == 1:
        block5 += 'execute unless score #{} used matches 1 if score #required_letter vars matches 0..1 unless score #{}_words used < #{}_words_max vars run function wordsmith:detect/punish_dead_end\n'.format(block_formal_name_score, letter_end, letter_end)
    else:
        block5 += 'execute unless score #{} used matches 1 if score #required_letter vars matches 0 unless score #{}_words used < #{}_words_max vars run function wordsmith:detect/punish_dead_end\n'.format(block_formal_name_score, letter_end, letter_end)
        block5 += 'execute unless score #{} used matches 1 if score #required_letter vars matches {} unless score #{}_words used < #{}_words_max vars run function wordsmith:detect/punish_dead_end\n'.format(block_formal_name_score, letter_start_num, letter_end, letter_end)
    block5 += '\n# Call second function if letter correct, next letter available, and if not used\n'
    if letter_start_num == 1:
        block5 += 'execute if score #required_letter vars matches 0..1 unless score #{} used matches 1 if score #{}_words used < #{}_words_max vars run function wordsmith:detect/blocks/{}2\n'.format(block_formal_name_score, letter_end, letter_end, block_name)
    else:
        block5 += 'execute if score #required_letter vars matches 0 unless score #{} used matches 1 if score #{}_words used < #{}_words_max vars run function wordsmith:detect/blocks/{}2\n'.format(block_formal_name_score, letter_end, letter_end, block_name)
        block5 += 'execute if score #required_letter vars matches {} unless score #{} used matches 1 if score #{}_words used < #{}_words_max vars run function wordsmith:detect/blocks/{}2\n'.format(letter_start_num, block_formal_name_score, letter_end, letter_end, block_name)
    block5 += '\n# Set last submission and used\n'
    block5 += 'scoreboard players set @s last_submission {}\n'.format(n)

    block6 = '# Set word count and word submitted\n'
    block6 += 'scoreboard players set #word_submitted vars 1\n'
    block6 += 'scoreboard players add #{}_words used 1\n'.format(block_name[0].lower())
    block6 += '\n# Call replacement function\n'
    block6 += 'function wordsmith:detect/blocks/{}3\n'.format(block_name)
    block6 += '\n# If block not replaced, summon some\n'
    block6 += 'scoreboard players operation #curr_block_spawning_density vars = #block_spawning_density vars\n'
    block6 += 'execute if score #blocks_killed1 vars matches 0 if score #blocks_killed2 vars matches 0 if score #blocks_replaced1 vars matches 0 if score #blocks_replaced2 vars matches 0 if score #blocks_replaced3 vars matches 0 if score #blocks_replaced4 vars matches 0 if score #blocks_replaced5 vars matches 0 if score #blocks_replaced6 vars matches 0 if score #blocks_replaced7 vars matches 0 if score #blocks_replaced8 vars matches 0 if score #blocks_replaced9 vars matches 0 if score #blocks_replaced10 vars matches 0 if score #blocks_replaced11 vars matches 0 if score #blocks_replaced12 vars matches 0 if score #blocks_replaced13 vars matches 0 if score #blocks_replaced14 vars matches 0 if score #blocks_replaced15 vars matches 0 if score #blocks_replaced16 vars matches 0 if score #blocks_cleared1 vars matches 0 run schedule function wordsmith:detect/blocks/{}4 1t\n'.format(block_name)
    block6 += '\n# Set required letter\n'
    block6 += 'scoreboard players set #required_letter vars {}\n'.format(letter_end_num)
    block6 += '\n# Tell players the good news!\n'
    block6 += 'execute if entity @s[team=Red] run tellraw @a {"selector":"@s","color":"red","extra":[{"text":" submitted a word: "},{"text":"' + block_formal_name + '","bold":true}]}\n'
    block6 += 'execute if entity @s[team=Blue] run tellraw @a {"selector":"@s","color":"blue","extra":[{"text":" submitted a word: "},{"text":"' + block_formal_name + '","bold":true}]}\n'
    block6 += 'execute if entity @s[team=Green] run tellraw @a {"selector":"@s","color":"green","extra":[{"text":" submitted a word: "},{"text":"' + block_formal_name + '","bold":true}]}\n'
    block6 += 'execute if entity @s[team=Yellow] run tellraw @a {"selector":"@s","color":"yellow","extra":[{"text":" submitted a word: "},{"text":"' + block_formal_name + '","bold":true}]}\n'
    block6 += '\n# Start the next turn.\n'
    block6 += 'schedule function wordsmith:turn/get_permutation 2t'

    # print('execute unless score #word_submitted vars matches 1 unless score @s last_submission matches ' + str(n) + ' if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + block_formal_name + '"]}}]}] run function wordsmith:detect/blocks/' + block_name)

    wr = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks/{}5.mcfunction'.format(block_name), 'w')
    wr.write(block5)
    wr.close()

    wr = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks/{}6.mcfunction'.format(block_name), 'w')
    wr.write(block6)
    wr.close()

    n+= 1