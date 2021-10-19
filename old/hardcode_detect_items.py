import json
import os

m = json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/resourcepacks/Default Resource Pack/assets/minecraft/lang', 'en_us.json'), 'r'))

n = 756

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
    if not lang_name.startswith('item.minecraft.'):
        continue
    item_name = lang_name[15:]
    if '.' in item_name:
        continue

    item_formal_name = m[lang_name].lower()
    item_formal_name_score = item_formal_name.replace(' ', '_')
    letter_end = item_formal_name[-1]
    letter_start_num = letter_nums[item_formal_name[0].lower()]
    letter_end_num = letter_nums[item_formal_name[-1]]

    if not os.path.isfile('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/items/{}.mcfunction'.format(item_name)):
        continue

    item1 = '# Call punish_used function, if used\n'
    item1 += 'execute if score #{} used matches 1 run function wordsmith:detect/punish_used\n'.format(item_formal_name_score)
    item1 += '\n# Call punish_wrong_letter function, if wrong letter and not used\n'
    if letter_start_num == 1:
        item1 += 'execute unless score #{} used matches 1 unless score #required_letter vars matches 0..1 run function wordsmith:detect/punish_wrong_letter\n'.format(item_formal_name_score)
    else:
        item1 += 'execute unless score #{} used matches 1 unless score #required_letter vars matches 0 unless score #required_letter vars matches {} run function wordsmith:detect/punish_wrong_letter\n'.format(item_formal_name_score, letter_start_num)
    item1 += '\n# Call punish_dead_end function, if word would lead to a dead end\n'
    if letter_start_num == 1:
        item1 += 'execute unless score #{} used matches 1 if score #required_letter vars matches 0..1 unless score #{}_words used < #{}_words_max vars run function wordsmith:detect/punish_dead_end\n'.format(item_formal_name_score, letter_end, letter_end)
    else:
        item1 += 'execute unless score #{} used matches 1 if score #required_letter vars matches 0 unless score #{}_words used < #{}_words_max vars run function wordsmith:detect/punish_dead_end\n'.format(item_formal_name_score, letter_end, letter_end)
        item1 += 'execute unless score #{} used matches 1 if score #required_letter vars matches {} unless score #{}_words used < #{}_words_max vars run function wordsmith:detect/punish_dead_end\n'.format(item_formal_name_score, letter_start_num, letter_end, letter_end)
    item1 += '\n# Call second function if letter correct, next letter available, and if not used\n'
    if letter_start_num == 1:
        item1 += 'execute if score #required_letter vars matches 0..1 unless score #{} used matches 1 if score #{}_words used < #{}_words_max vars run function wordsmith:detect/items/{}2\n'.format(item_formal_name_score, letter_end, letter_end, item_name)
    else:
        item1 += 'execute if score #required_letter vars matches 0 unless score #{} used matches 1 if score #{}_words used < #{}_words_max vars run function wordsmith:detect/items/{}2\n'.format(item_formal_name_score, letter_end, letter_end, item_name)
        item1 += 'execute if score #required_letter vars matches {} unless score #{} used matches 1 if score #{}_words used < #{}_words_max vars run function wordsmith:detect/items/{}2\n'.format(letter_start_num, item_formal_name_score, letter_end, letter_end, item_name)
    item1 += '\n# Set last submission and used\n'
    item1 += 'scoreboard players set @s last_submission {}\n'.format(n)

    item2 = '# Set word count and word submitted\n'
    item2 += 'scoreboard players set #word_submitted vars 1\n'
    item2 += 'scoreboard players add #{}_words used 1\n'.format(item_name[0].lower())
    item2 += '\n# Call replacement function\n'
    item2 += 'function wordsmith:detect/items/{}3\n'.format(item_name)
    item2 += '\n# If item not replaced, summon some\n'
    item2 += 'scoreboard players operation #curr_item_spawning_density vars = #item_spawning_density vars\n'
    item2 += 'execute if score #items_killed vars matches 0 if score #items_cleared vars matches 0 run schedule function wordsmith:detect/items/{}4 1t\n'.format(item_name)
    item2 += '\n# Set required letter\n'
    item2 += 'scoreboard players set #required_letter vars {}\n'.format(letter_end_num)
    item2 += '\n# Tell players the good news!\n'
    item2 += 'execute if entity @s[team=Red] run tellraw @a {"selector":"@s","color":"red","extra":[{"text":" submitted a word: "},{"text":"' + item_formal_name + '","bold":true}]}\n'
    item2 += 'execute if entity @s[team=Blue] run tellraw @a {"selector":"@s","color":"blue","extra":[{"text":" submitted a word: "},{"text":"' + item_formal_name + '","bold":true}]}\n'
    item2 += 'execute if entity @s[team=Green] run tellraw @a {"selector":"@s","color":"green","extra":[{"text":" submitted a word: "},{"text":"' + item_formal_name + '","bold":true}]}\n'
    item2 += 'execute if entity @s[team=Yellow] run tellraw @a {"selector":"@s","color":"yellow","extra":[{"text":" submitted a word: "},{"text":"' + item_formal_name + '","bold":true}]}\n'
    item2 += '\n# Start the next turn.\n'
    item2 += 'schedule function wordsmith:turn/get_permutation 2t'

    item3 = '# Attempt to fill / kill / clear in item\n'
    item3 += 'execute store result score #items_killed vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + item_name + '"}}]\n'
    item3 += 'execute store result score #items_cleared vars run clear @a minecraft:{}'.format(item_name)

    item4 = '# {} density is 1x\n'.format(item_formal_name[0].upper() + item_formal_name[1:].lower())
    item4 += '# Summon armor stands\n'
    item4 += 'scoreboard players operation #spreaded_armor_stands vars = #curr_item_spawning_density vars\n'
    item4 += 'function wordsmith:detect/spread_armor_stands_r1\n'
    item4 += '\n# Summon item\n'
    item4 += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + item_name + '",Count:1b}}\n'
    item4 += '\n# Give fancy particle for the current team\n'
    item4 += 'execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~10.375 ~ 0.4 0.4 0.4 1 60\n'
    item4 += 'execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~10.375 ~ 0.4 0.4 0.4 1 60\n'
    item4 += 'execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~10.375 ~ 0.4 0.4 0.4 1 60\n'
    item4 += 'execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~10.375 ~ 0.4 0.4 0.4 1 60\n'
    item4 += '\n# Kill the armor stands\n'
    item4 += 'kill @e[type=minecraft:armor_stand,tag=spawner]'

    # print('execute unless score #word_submitted vars matches 1 unless score @s last_submission matches ' + str(n) + ' if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + item_formal_name + '"]}}]}] run function wordsmith:detect/items/' + item_name)

    wr = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/items/{}.mcfunction'.format(item_name), 'w')
    wr.write(item1)
    wr.close()

    wr = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/items/{}2.mcfunction'.format(item_name), 'w')
    wr.write(item2)
    wr.close()

    wr = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/items/{}3.mcfunction'.format(item_name), 'w')
    wr.write(item3)
    wr.close()

    wr = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/items/{}4.mcfunction'.format(item_name), 'w')
    wr.write(item4)
    wr.close()

    n+= 1