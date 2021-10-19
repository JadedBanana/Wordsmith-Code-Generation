import json
import os

m = {
   'emerald_block': 'emerald block',
   'diamond_block': 'diamond block',
   'gold_block': 'gold block',
   'smooth_quartz': 'smooth quartz',
   'redstone_block': 'redstone block'
}

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

for block_name in m:
    print('execute unless score #word_submitted vars matches 1 unless score @s last_submission matches ' + str(n) + ' if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + m[block_name].lower() + '"]}}]}] run function wordsmith:detect/blocks/' + block_name)

    block1 = '''# Call second function if letter correct and if not used''' + ('''
execute if score #required_letter vars matches 0 unless score #''' + m[block_name].lower().replace(' ', '_') + ''' used matches 1 run function wordsmith:detect/blocks/{}4
execute if score #required_letter vars matches {} unless score #'''.format(block_name,letter_nums[m[block_name].lower()[0]]) + m[block_name].lower().replace(' ', '_') + ''' used matches 1 run function wordsmith:detect/blocks/{}4'''.format(block_name) if letter_nums[m[block_name].lower()[0]] != 1 else '''
execute if score #required_letter vars matches 0..1 unless score #''' + m[block_name].lower().replace(' ', '_') + ''' used matches 1 run function wordsmith:detect/blocks/{}4'''.format(block_name)) + '''

# Call punish_used function, if used
execute if score #''' + block_name + ''' used matches 1 run function wordsmith:detect/punish_used

# Call punish_wrong_letter function, if wrong letter and not used
''' + ('execute unless score #''' + block_name + ''' used matches 1 if score #required_letter vars matches 1..{} run function wordsmith:detect/punish_wrong_letter'''.format(letter_nums[m[block_name].lower()[0]] - 1) if letter_nums[m[block_name].lower()[0]] > 2 else ('execute unless score #''' + block_name + ''' used matches 1 if score #required_letter vars matches 1 run function wordsmith:detect/punish_wrong_letter''' if letter_nums[m[block_name].lower()[0]] == 2 else ''))  + ('''
execute unless score #''' + block_name + ''' used matches 1 if score #required_letter vars matches {}..26 run function wordsmith:detect/punish_wrong_letter\n'''.format(letter_nums[m[block_name].lower()[0]] + 1) if letter_nums[m[block_name].lower()[0]] < 25 else ('''
execute unless score #''' + block_name + ''' used matches 1 if score #required_letter vars matches 26 run function wordsmith:detect/punish_wrong_letter\n''' if letter_nums[m[block_name].lower()[0]] == 25 else '''
''')) + '''
# Set last submission
scoreboard players set @s last_submission ''' + str(n) + '''

# Set used
scoreboard players set #''' + block_name + ' used 1'

    block2 = '''# Set scoreboard vars
scoreboard players set #word_submitted vars 1

# Attempt to fill in ''' + m[block_name].lower() + '''
execute store result score #blocks_killed1 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:'''+ block_name + '''"}}]
execute store result score #blocks_killed2 vars run kill @e[type=minecraft:falling_block,nbt={BlockState:{Name:"minecraft:'''+ block_name + '''"}}]
execute store result score #blocks_replaced1 vars run fill ~-22 0 ~-22 ~22 15 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced2 vars run fill ~-22 16 ~-22 ~22 31 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced3 vars run fill ~-22 32 ~-22 ~22 47 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced4 vars run fill ~-22 48 ~-22 ~22 63 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced5 vars run fill ~-22 64 ~-22 ~22 79 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced6 vars run fill ~-22 80 ~-22 ~22 95 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced7 vars run fill ~-22 96 ~-22 ~22 111 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced8 vars run fill ~-22 112 ~-22 ~22 127 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced9 vars run fill ~-22 128 ~-22 ~22 143 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced10 vars run fill ~-22 144 ~-22 ~22 159 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced11 vars run fill ~-22 160 ~-22 ~22 175 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced12 vars run fill ~-22 176 ~-22 ~22 191 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced13 vars run fill ~-22 192 ~-22 ~22 207 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced14 vars run fill ~-22 208 ~-22 ~22 223 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced15 vars run fill ~-22 224 ~-22 ~22 239 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_replaced16 vars run fill ~-22 240 ~-22 ~22 255 ~22 air replace minecraft:''' + block_name + '''
execute store result score #blocks_cleared1 vars run clear @a minecraft:''' + block_name + '''

# If ''' + m[block_name].lower() + ''' not replaced, summon some
execute if score #blocks_killed1 vars matches 0 if score #blocks_killed2 vars matches 0 if score #blocks_replaced1 vars matches 0 if score #blocks_replaced2 vars matches 0 if score #blocks_replaced3 vars matches 0 if score #blocks_replaced4 vars matches 0 if score #blocks_replaced5 vars matches 0 if score #blocks_replaced6 vars matches 0 if score #blocks_replaced7 vars matches 0 if score #blocks_replaced8 vars matches 0 if score #blocks_replaced9 vars matches 0 if score #blocks_replaced10 vars matches 0 if score #blocks_replaced11 vars matches 0 if score #blocks_replaced12 vars matches 0 if score #blocks_replaced13 vars matches 0 if score #blocks_replaced14 vars matches 0 if score #blocks_replaced15 vars matches 0 if score #blocks_replaced16 vars matches 0 if score #blocks_cleared1 vars matches 0 run schedule function wordsmith:detect/blocks/''' + block_name +'''5 1t

# Set required letter
scoreboard players set #required_letter vars ''' + str(letter_nums[m[block_name].lower()[-1]]) + '''

# Tell players the good news!
execute if entity @s[team=Red] run tellraw @a {"selector":"@s","color":"red","extra":[{"text":" submitted the word: "},{"text":"''' + m[block_name].lower() + '''","bold":true}]}
execute if entity @s[team=Blue] run tellraw @a {"selector":"@s","color":"blue","extra":[{"text":" submitted the word: "},{"text":"''' + m[block_name].lower() + '''","bold":true}]}
execute if entity @s[team=Green] run tellraw @a {"selector":"@s","color":"green","extra":[{"text":" submitted the word: "},{"text":"''' + m[block_name].lower() + '''","bold":true}]}
execute if entity @s[team=Yellow] run tellraw @a {"selector":"@s","color":"yellow","extra":[{"text":" submitted the word: "},{"text":"''' + m[block_name].lower() + '''","bold":true}]}

# Start the next turn.
schedule function wordsmith:turn/get_permutation 2t'''

    block3 = '''# ''' + m[block_name][0] + m[block_name].lower()[1:] + ''' density is 1x
# Summon armor stands
scoreboard players operation #spreaded_armor_stands vars = #block_spawning_density vars
function wordsmith:detect/spread_armor_stands_r1

# Summon block
execute at @e[type=minecraft:armor_stand,tag=spawner] run summon minecraft:falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:''' + block_name + '''"},Time:1}

# Give fancy particle for the current team
execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~10.5 ~ 0.5 0.5 0.5 1 100
execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~10.5 ~ 0.5 0.5 0.5 1 100
execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~10.5 ~ 0.5 0.5 0.5 1 100
execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~10.5 ~ 0.5 0.5 0.5 1 100

# Kill the armor stands
kill @e[type=minecraft:armor_stand,tag=spawner]

# Do all of that again
# Summon armor stands
scoreboard players operation #spreaded_armor_stands vars = #block_spawning_density vars
function wordsmith:detect/spread_armor_stands_r1

# Summon block
execute at @e[type=minecraft:armor_stand,tag=spawner] run summon minecraft:falling_block ~ ~12 ~ {BlockState:{Name:"minecraft:''' + block_name + '''"},Time:1}

# Give fancy particle for the current team
execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~12.5 ~ 0.5 0.5 0.5 1 100
execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~12.5 ~ 0.5 0.5 0.5 1 100
execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~12.5 ~ 0.5 0.5 0.5 1 100
execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~12.5 ~ 0.5 0.5 0.5 1 100

# Kill the armor stands
kill @e[type=minecraft:armor_stand,tag=spawner]'''

    r = open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks', block_name + '4.mcfunction'), 'w')
    r.write(block1)
    r.close()
    r = open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks', block_name + '5.mcfunction'), 'w')
    r.write(block2)
    r.close()
    n+= 1