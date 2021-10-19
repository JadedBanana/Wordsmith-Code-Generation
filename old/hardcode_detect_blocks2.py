import json
import os

m = json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/resourcepacks/Default Resource Pack/assets/minecraft/lang', 'en_us.json'), 'r'))

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

for lang_name in m:
    if not lang_name.startswith('block.minecraft.'):
        continue
    block_name = lang_name[16:]
    if '.' in block_name:
        continue

    block_formal_name = m[lang_name].lower()
    block_formal_name_score = block_formal_name.replace(' ', '_')
    letter_end = block_formal_name[-1]
    letter_start_num = letter_nums[block_formal_name[0].lower()]
    letter_end_num = letter_nums[block_formal_name[-1]]

    if not os.path.isfile('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks/{}.mcfunction'.format(block_name)):
        continue

    block1 = '# Call punish_used function, if used\n'
    block1 += 'execute if score #{} used matches 1 run function wordsmith:detect/punish_used\n'.format(block_formal_name_score)
    block1 += '\n# Call punish_wrong_letter function, if wrong letter and not used\n'
    if letter_start_num == 1:
        block1 += 'execute unless score #{} used matches 1 unless score #required_letter vars matches 0..1 run function wordsmith:detect/punish_wrong_letter\n'.format(block_formal_name_score)
    else:
        block1 += 'execute unless score #{} used matches 1 unless score #required_letter vars matches 0 unless score #required_letter vars matches {} run function wordsmith:detect/punish_wrong_letter\n'.format(block_formal_name_score, letter_start_num)
    block1 += '\n# Call punish_dead_end function, if word would lead to a dead end\n'
    if letter_start_num == 1:
        block1 += 'execute unless score #{} used matches 1 if score #required_letter vars matches 0..1 unless score #{}_words used < #{}_words_max vars run function wordsmith:detect/punish_dead_end\n'.format(block_formal_name_score, letter_end, letter_end)
    else:
        block1 += 'execute unless score #{} used matches 1 if score #required_letter vars matches 0 unless score #{}_words used < #{}_words_max vars run function wordsmith:detect/punish_dead_end\n'.format(block_formal_name_score, letter_end, letter_end)
        block1 += 'execute unless score #{} used matches 1 if score #required_letter vars matches {} unless score #{}_words used < #{}_words_max vars run function wordsmith:detect/punish_dead_end\n'.format(block_formal_name_score, letter_start_num, letter_end, letter_end)
    block1 += '\n# Call second function if letter correct, next letter available, and if not used\n'
    if letter_start_num == 1:
        block1 += 'execute if score #required_letter vars matches 0..1 unless score #{} used matches 1 if score #{}_words used < #{}_words_max vars run function wordsmith:detect/blocks/{}2\n'.format(block_formal_name_score, letter_end, letter_end, block_name)
    else:
        block1 += 'execute if score #required_letter vars matches 0 unless score #{} used matches 1 if score #{}_words used < #{}_words_max vars run function wordsmith:detect/blocks/{}2\n'.format(block_formal_name_score, letter_end, letter_end, block_name)
        block1 += 'execute if score #required_letter vars matches {} unless score #{} used matches 1 if score #{}_words used < #{}_words_max vars run function wordsmith:detect/blocks/{}2\n'.format(letter_start_num, block_formal_name_score, letter_end, letter_end, block_name)
    block1 += '\n# Set last submission and used\n'
    block1 += 'scoreboard players set @s last_submission {}\n'.format(n)

    block2 = '# Set word count and word submitted\n'
    block2 += 'scoreboard players set #word_submitted vars 1\n'
    block2 += 'scoreboard players add #{}_words used 1\n'.format(block_name[0].lower())
    block2 += '\n# Call replacement function\n'
    block2 += 'function wordsmith:detect/blocks/{}3\n'.format(block_name)
    block2 += '\n# If block not replaced, summon some\n'
    block2 += 'scoreboard players operation #curr_block_spawning_density vars = #block_spawning_density vars\n'
    block2 += 'execute if score #blocks_killed1 vars matches 0 if score #blocks_killed2 vars matches 0 if score #blocks_replaced1 vars matches 0 if score #blocks_replaced2 vars matches 0 if score #blocks_replaced3 vars matches 0 if score #blocks_replaced4 vars matches 0 if score #blocks_replaced5 vars matches 0 if score #blocks_replaced6 vars matches 0 if score #blocks_replaced7 vars matches 0 if score #blocks_replaced8 vars matches 0 if score #blocks_replaced9 vars matches 0 if score #blocks_replaced10 vars matches 0 if score #blocks_replaced11 vars matches 0 if score #blocks_replaced12 vars matches 0 if score #blocks_replaced13 vars matches 0 if score #blocks_replaced14 vars matches 0 if score #blocks_replaced15 vars matches 0 if score #blocks_replaced16 vars matches 0 if score #blocks_cleared1 vars matches 0 run schedule function wordsmith:detect/blocks/{}4 1t\n'.format(block_name)
    block2 += '\n# Set required letter\n'
    block2 += 'scoreboard players set #required_letter vars {}\n'.format(letter_end_num)
    block2 += '\n# Tell players the good news!\n'
    block2 += 'execute if entity @s[team=Red] run tellraw @a {"selector":"@s","color":"red","extra":[{"text":" submitted a word: "},{"text":"' + block_formal_name + '","bold":true}]}\n'
    block2 += 'execute if entity @s[team=Blue] run tellraw @a {"selector":"@s","color":"blue","extra":[{"text":" submitted a word: "},{"text":"' + block_formal_name + '","bold":true}]}\n'
    block2 += 'execute if entity @s[team=Green] run tellraw @a {"selector":"@s","color":"green","extra":[{"text":" submitted a word: "},{"text":"' + block_formal_name + '","bold":true}]}\n'
    block2 += 'execute if entity @s[team=Yellow] run tellraw @a {"selector":"@s","color":"yellow","extra":[{"text":" submitted a word: "},{"text":"' + block_formal_name + '","bold":true}]}\n'
    block2 += '\n# Start the next turn.\n'
    block2 += 'schedule function wordsmith:turn/get_permutation 2t'

    block3 = '# Attempt to fill / kill / clear in block\n'
    block3 += 'execute store result score #blocks_killed1 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + block_name + '"}}]\n'
    block3 += 'execute store result score #blocks_killed2 vars run kill @e[type=minecraft:falling_block,nbt={BlockState:{Name:"minecraft:' + block_name + '"}}]\n'
    for i in range(16):
        block3 += 'execute store result score #blocks_replaced{} vars run fill ~-22 {} ~-22 ~22 {} ~22 air replace minecraft:{}\n'.format(i + 1, i * 16, (i + 1) * 16 - 1, block_name)
    block3 += 'execute store result score #blocks_cleared1 vars run clear @a minecraft:{}'.format(block_name)

    block4 = '# {} density is 1x\n'.format(block_formal_name[0].upper() + block_formal_name[1:].lower())
    block4 += '# Summon armor stands\n'
    block4 += 'scoreboard players operation #spreaded_armor_stands vars = #curr_block_spawning_density vars\n'
    block4 += 'function wordsmith:detect/spread_armor_stands_r1\n'
    block4 += '\n# Summon block\n'
    block4 += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon minecraft:falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + block_name + '"},Time:1}\n'
    block4 += '\n# Give fancy particle for the current team\n'
    block4 += 'execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~10.5 ~ 0.5 0.5 0.5 1 100\n'
    block4 += 'execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~10.5 ~ 0.5 0.5 0.5 1 100\n'
    block4 += 'execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~10.5 ~ 0.5 0.5 0.5 1 100\n'
    block4 += 'execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~10.5 ~ 0.5 0.5 0.5 1 100\n'
    block4 += '\n# Kill the armor stands\n'
    block4 += 'kill @e[type=minecraft:armor_stand,tag=spawner]\n'
    block4 += '\n# Do all of that again\n'
    block4 += '# Summon armor stands\n'
    block4 += 'scoreboard players operation #spreaded_armor_stands vars = #block_spawning_density vars\n'
    block4 += 'function wordsmith:detect/spread_armor_stands_r1\n'
    block4 += '\n# Summon block\n'
    block4 += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon minecraft:falling_block ~ ~12 ~ {BlockState:{Name:"minecraft:' + block_name + '"},Time:1}\n'
    block4 += '\n# Give fancy particle for the current team\n'
    block4 += 'execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~12.5 ~ 0.5 0.5 0.5 1 100\n'
    block4 += 'execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~12.5 ~ 0.5 0.5 0.5 1 100\n'
    block4 += 'execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~12.5 ~ 0.5 0.5 0.5 1 100\n'
    block4 += 'execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~12.5 ~ 0.5 0.5 0.5 1 100\n'
    block4 += '\n# Kill the armor stands\n'
    block4 += 'kill @e[type=minecraft:armor_stand,tag=spawner]'

    # print('execute unless score #word_submitted vars matches 1 unless score @s last_submission matches ' + str(n) + ' if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + block_formal_name + '"]}}]}] run function wordsmith:detect/blocks/' + block_name)

    wr = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks/{}.mcfunction'.format(block_name), 'w')
    wr.write(block1)
    wr.close()

    wr = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks/{}2.mcfunction'.format(block_name), 'w')
    wr.write(block2)
    wr.close()

    wr = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks/{}3.mcfunction'.format(block_name), 'w')
    wr.write(block3)
    wr.close()

    wr = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks/{}4.mcfunction'.format(block_name), 'w')
    wr.write(block4)
    wr.close()

    n+= 1