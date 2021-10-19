import words
word_list = words.words_en

enchant_str = '''# Copy inventory
function wordsmith:detect/item/enchant/copy_inv_part1

# Remove enchant_goes_here for hotbar + top 2 rows of items
execute store success score #enchant_removed1 vars run data remove block ~ 255 ~ Items[{Slot:0b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed2 vars run data remove block ~ 255 ~ Items[{Slot:0b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed3 vars run data remove block ~ 255 ~ Items[{Slot:1b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed4 vars run data remove block ~ 255 ~ Items[{Slot:1b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed5 vars run data remove block ~ 255 ~ Items[{Slot:2b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed6 vars run data remove block ~ 255 ~ Items[{Slot:2b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed7 vars run data remove block ~ 255 ~ Items[{Slot:3b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed8 vars run data remove block ~ 255 ~ Items[{Slot:3b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed9 vars run data remove block ~ 255 ~ Items[{Slot:4b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed10 vars run data remove block ~ 255 ~ Items[{Slot:4b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed11 vars run data remove block ~ 255 ~ Items[{Slot:5b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed12 vars run data remove block ~ 255 ~ Items[{Slot:5b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed13 vars run data remove block ~ 255 ~ Items[{Slot:6b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed14 vars run data remove block ~ 255 ~ Items[{Slot:6b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed15 vars run data remove block ~ 255 ~ Items[{Slot:7b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed16 vars run data remove block ~ 255 ~ Items[{Slot:7b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed17 vars run data remove block ~ 255 ~ Items[{Slot:8b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed18 vars run data remove block ~ 255 ~ Items[{Slot:8b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed19 vars run data remove block ~ 255 ~ Items[{Slot:9b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed20 vars run data remove block ~ 255 ~ Items[{Slot:9b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed21 vars run data remove block ~ 255 ~ Items[{Slot:10b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed22 vars run data remove block ~ 255 ~ Items[{Slot:10b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed23 vars run data remove block ~ 255 ~ Items[{Slot:11b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed24 vars run data remove block ~ 255 ~ Items[{Slot:11b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed25 vars run data remove block ~ 255 ~ Items[{Slot:12b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed26 vars run data remove block ~ 255 ~ Items[{Slot:12b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed27 vars run data remove block ~ 255 ~ Items[{Slot:13b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed28 vars run data remove block ~ 255 ~ Items[{Slot:13b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed29 vars run data remove block ~ 255 ~ Items[{Slot:14b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed30 vars run data remove block ~ 255 ~ Items[{Slot:14b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed31 vars run data remove block ~ 255 ~ Items[{Slot:15b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed32 vars run data remove block ~ 255 ~ Items[{Slot:15b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed33 vars run data remove block ~ 255 ~ Items[{Slot:16b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed34 vars run data remove block ~ 255 ~ Items[{Slot:16b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed35 vars run data remove block ~ 255 ~ Items[{Slot:17b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed36 vars run data remove block ~ 255 ~ Items[{Slot:17b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed37 vars run data remove block ~ 255 ~ Items[{Slot:18b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed38 vars run data remove block ~ 255 ~ Items[{Slot:18b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed39 vars run data remove block ~ 255 ~ Items[{Slot:19b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed40 vars run data remove block ~ 255 ~ Items[{Slot:19b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed41 vars run data remove block ~ 255 ~ Items[{Slot:20b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed42 vars run data remove block ~ 255 ~ Items[{Slot:20b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed43 vars run data remove block ~ 255 ~ Items[{Slot:21b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed44 vars run data remove block ~ 255 ~ Items[{Slot:21b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed45 vars run data remove block ~ 255 ~ Items[{Slot:22b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed46 vars run data remove block ~ 255 ~ Items[{Slot:22b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed47 vars run data remove block ~ 255 ~ Items[{Slot:23b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed48 vars run data remove block ~ 255 ~ Items[{Slot:23b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed49 vars run data remove block ~ 255 ~ Items[{Slot:24b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed50 vars run data remove block ~ 255 ~ Items[{Slot:24b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed51 vars run data remove block ~ 255 ~ Items[{Slot:25b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed52 vars run data remove block ~ 255 ~ Items[{Slot:25b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed53 vars run data remove block ~ 255 ~ Items[{Slot:26b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed54 vars run data remove block ~ 255 ~ Items[{Slot:26b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]

# Copy inventory 2
function wordsmith:detect/item/enchant/copy_inv_part2

# Remove enchant_goes_here for bottom row of items
execute store success score #enchant_removed55 vars run data remove block ~ 255 ~ Items[{Slot:0b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed56 vars run data remove block ~ 255 ~ Items[{Slot:0b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed57 vars run data remove block ~ 255 ~ Items[{Slot:1b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed58 vars run data remove block ~ 255 ~ Items[{Slot:1b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed59 vars run data remove block ~ 255 ~ Items[{Slot:2b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed60 vars run data remove block ~ 255 ~ Items[{Slot:2b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed61 vars run data remove block ~ 255 ~ Items[{Slot:3b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed62 vars run data remove block ~ 255 ~ Items[{Slot:3b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed63 vars run data remove block ~ 255 ~ Items[{Slot:4b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed64 vars run data remove block ~ 255 ~ Items[{Slot:4b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed65 vars run data remove block ~ 255 ~ Items[{Slot:5b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed66 vars run data remove block ~ 255 ~ Items[{Slot:5b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed67 vars run data remove block ~ 255 ~ Items[{Slot:6b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed68 vars run data remove block ~ 255 ~ Items[{Slot:6b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed69 vars run data remove block ~ 255 ~ Items[{Slot:7b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed70 vars run data remove block ~ 255 ~ Items[{Slot:7b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed71 vars run data remove block ~ 255 ~ Items[{Slot:8b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed72 vars run data remove block ~ 255 ~ Items[{Slot:8b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]

# Copy inventory 3
function wordsmith:detect/item/enchant/copy_inv_part3

# Remove enchant_goes_here for armor slots
execute store success score #enchant_removed73 vars run data remove block ~ 255 ~ Items[{Slot:0b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed74 vars run data remove block ~ 255 ~ Items[{Slot:0b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed75 vars run data remove block ~ 255 ~ Items[{Slot:1b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed76 vars run data remove block ~ 255 ~ Items[{Slot:1b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed77 vars run data remove block ~ 255 ~ Items[{Slot:2b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed78 vars run data remove block ~ 255 ~ Items[{Slot:2b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed79 vars run data remove block ~ 255 ~ Items[{Slot:3b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed80 vars run data remove block ~ 255 ~ Items[{Slot:3b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]

# Copy inventory 4
function wordsmith:detect/item/enchant/copy_inv_part4

# Remove enchant_goes_here for offhand
execute store success score #enchant_removed81 vars run data remove block ~ 255 ~ Items[{Slot:0b}].tag.Enchantments[{id:"minecraft:enchant_goes_here"}]
execute store success score #enchant_removed82 vars run data remove block ~ 255 ~ Items[{Slot:0b}].tag.StoredEnchantments[{id:"minecraft:enchant_goes_here"}]

# Copy inventory 5
function wordsmith:detect/item/enchant/copy_inv_part5'''

for entry in word_list:
    for entry2 in word_list[entry]:
        if 'manual' in entry2:
            continue

        if 'item' in entry2:

            if 'potion' in entry2:
                if entry2['item'].endswith('_lingering_pot'):
                    item_type = 'lingering_potion'
                    potion_type = entry2['item'][:-14]
                elif entry2['item'].endswith('_splash_pot'):
                    item_type = 'splash_potion'
                    potion_type = entry2['item'][:-11]
                else:
                    item_type = 'potion'
                    potion_type = entry2['item'][:-4]
                item1 = '# Attempt to kill / clear item'
                item1 += '\nexecute store result score #potions_killed1 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:' + potion_type + '"}}}]'
                if 'long' in entry2:
                    item1 += '\nexecute store result score #potions_killed2 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:long_' + potion_type + '"}}}]'
                    if 'strong' in entry2:
                        item1 += '\nexecute store result score #potions_killed3 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:strong_' + potion_type + '"}}}]'
                elif 'strong' in entry2:
                    item1 += '\nexecute store result score #potions_killed2 vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:strong_' + potion_type + '"}}}]'
                if item_type == 'splash_potion':
                    item1 += '\nexecute store result score #potions_killed4 vars run kill @e[type=minecraft:potion,nbt={Item:{tag:{Potion:"minecraft:' + potion_type + '"}}}]'
                item1 += '\nexecute store result score #potions_cleared1 vars run clear @a minecraft:' + item_type + '{Potion:"minecraft:' + potion_type + '"}'
                if 'long' in entry2:
                    item1 += '\nexecute store result score #potions_cleared2 vars run clear @a minecraft:' + item_type + '{Potion:"minecraft:long_' + potion_type + '"}'
                    if 'strong' in entry2:
                        item1 += '\nexecute store result score #potions_cleared3 vars run clear @a minecraft:' + item_type + '{Potion:"minecraft:strong_' + potion_type + '"}'
                elif 'strong' in entry2:
                    item1 += '\nexecute store result score #potions_cleared2 vars run clear @a minecraft:' + item_type + '{Potion:"minecraft:strong_' + potion_type + '"}'
                item1 += '\n\n# If item not killed / cleared, summon some'
                item1 += '\nscoreboard players operation #curr_item_spawning_density vars = #item_spawning_density vars'
                item1 += '\nexecute if score #potions_killed1 vars matches 0 '
                if 'long' in entry2:
                    if 'strong' in entry2:
                        item1 += 'if score #potions_killed2 vars matches 0 if score #potions_killed3 vars matches 0' + (' if score #potions_killed4 vars matches 0' if item_type == 'splash_potion' else '') + ' if score #potions_cleared1 vars matches 0 if score #potions_cleared2 vars matches 0 if score #potions_cleared3 vars matches 0 run schedule function wordsmith:detect/item/{}2 1t'.format(entry2['item'])
                    else:
                        item1 += 'if score #potions_killed2 vars matches 0' + (' if score #potions_killed4 vars matches 0' if item_type == 'splash_potion' else '') + ' if score #potions_cleared1 vars matches 0 if score #potions_cleared2 vars matches 0 run schedule function wordsmith:detect/item/{}2 1t'.format(entry2['item'])
                elif 'strong' in entry2:
                    item1 += 'if score #potions_killed2 vars matches 0' + (' if score #potions_killed4 vars matches 0' if item_type == 'splash_potion' else '') + ' if score #potions_cleared1 vars matches 0 if score #potions_cleared2 vars matches 0 run schedule function wordsmith:detect/item/{}2 1t'.format(entry2['item'])
                else:
                    item1 += ('if score #potions_killed4 vars matches 0 ' if item_type == 'splash_potion' else '') + 'if score #potions_cleared1 vars matches 0 run schedule function wordsmith:detect/item/{}2 1t'.format(entry2['item'])

                item2 = '# Summon armor stands\n'
                item2 += 'scoreboard players operation #spreaded_armor_stands vars = #curr_item_spawning_density vars\n'
                item2 += 'function wordsmith:detect/spread_armor_stands_r1\n'
                if 'long' in entry2:
                    if 'strong' in entry2:
                        item2 += '\n# Get RNG roll for potion type\n'
                        item2 += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMin 0\n'
                        item2 += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMax 3\n'
                        item2 += 'execute as @e[type=minecraft:armor_stand,tag=spawner] run function jrng:roll\n'
                        item2 += '\n# Summon item\n'
                        item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:' + potion_type + '"},Count:1b}}\n'
                        item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:long_' + potion_type + '"},Count:1b}}\n'
                        item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:strong_' + potion_type + '"},Count:1b}}\n'
                    else:
                        item2 += '\n# Get RNG roll for potion type\n'
                        item2 += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMin 0\n'
                        item2 += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMax 2\n'
                        item2 += 'execute as @e[type=minecraft:armor_stand,tag=spawner] run function jrng:roll\n'
                        item2 += '\n# Summon item\n'
                        item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:' + potion_type + '"},Count:1b}}\n'
                        item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:long_' + potion_type + '"},Count:1b}}\n'
                elif 'strong' in entry2:
                    item2 += '\n# Get RNG roll for potion type\n'
                    item2 += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMin 0\n'
                    item2 += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMax 2\n'
                    item2 += 'execute as @e[type=minecraft:armor_stand,tag=spawner] run function jrng:roll\n'
                    item2 += '\n# Summon item\n'
                    item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:' + potion_type + '"},Count:1b}}\n'
                    item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:strong_' + potion_type + '"},Count:1b}}\n'
                else:
                    item2 += '\n# Summon item\n'
                    item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + item_type + '",tag:{Potion:"minecraft:' + potion_type + '"},Count:1b}}\n'
                item2 += '\n# Give fancy particle for the current team\n'
                item2 += 'execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += 'execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += 'execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += 'execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += '\n# Kill the armor stands\n'
                item2 += 'kill @e[type=minecraft:armor_stand,tag=spawner]'
                item2 += '\n\n# Do all of that again\n' + item2.replace('~10', '~12')

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}.mcfunction'.format(entry2['item'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(item1)
                rb.close()

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}2.mcfunction'.format(entry2['item'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(item2)
                rb.close()

            elif 'enchant' in entry2:
                item1 = '# Set scoreboard value\n'
                item1 += 'scoreboard players set #enchant_removed_inv_item vars 0\n'
                item1 += '\n# Kill enchanted book items\n'
                item1 += 'execute store result score #enchant_removed_book vars run kill @e[type=item,nbt={Item:{id:"minecraft:enchanted_book",tag:{StoredEnchantments:[{"id":"minecraft:' + entry2['item'] + '"}]}}}]\n'
                item1 += '\n# Get rid of enchants from enchanted normal items\n'
                item1 += 'execute store result score #enchant_removed_item vars as @e[type=item] run data remove entity @s Item.tag.Enchantments[{id:"minecraft:' + entry2['item'] + '"}]\n'
                item1 += '\n# Clear enchanted book items in player inventories\n'
                item1 += 'execute store result score #enchant_removed_inv_book vars run clear @a minecraft:enchanted_book{StoredEnchantments:[{"id":"minecraft:' + entry2['item'] + '"}]}\n'
                item1 += '\n# Get rid of enchants from enchanted items in player inventories\n'
                item1 += 'execute if entity @a[nbt={Inventory:[{tag:{Enchantments:[{id:"minecraft:' + entry2['item'] + '"}]}}]}] run scoreboard players set #enchant_removed_inv_item vars 1\n'
                item1 += 'item modify entity @a hotbar.0 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a hotbar.1 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a hotbar.2 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a hotbar.3 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a hotbar.4 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a hotbar.5 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a hotbar.6 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a hotbar.7 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a hotbar.8 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a hotbar.0 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.0 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.1 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.2 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.3 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.4 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.5 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.6 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.7 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.8 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.9 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.10 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.11 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.12 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.13 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.14 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.15 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.16 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.17 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.18 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.19 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.20 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.21 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.22 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.23 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.24 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.25 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a inventory.26 wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a armor.head wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a armor.chest wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a armor.legs wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a armor.feet wordsmith:' + entry2['item'] + '\n'
                item1 += 'item modify entity @a weapon.offhand wordsmith:' + entry2['item'] + '\n'
                item1 += '\n# Schedule next'
                item1 += '\nexecute if score #enchant_removed_book vars matches 0 if score #enchant_removed_item vars matches 0 if score #enchant_removed_inv_book vars matches 0 if score #enchant_removed_inv_item vars matches 0 run schedule function wordsmith:detect/item/' + entry2['item'] + '2 1t'

                item2 = '# Summon armor stands\n'
                item2 += 'scoreboard players operation #spreaded_armor_stands vars = #curr_item_spawning_density vars\n'
                item2 += 'function wordsmith:detect/spread_armor_stands_r1\n'
                if 'max_level' in entry2 and entry2['max_level'] > 1:
                    max_level = entry2['max_level']
                    item2 += '\n# Get RNG roll for enchant level\n'
                    item2 += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMin 0\n'
                    item2 += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMax {}\n'.format(max_level)
                    item2 += 'execute as @e[type=minecraft:armor_stand,tag=spawner] run function jrng:roll\n'
                    item2 += '\n# Summon enchanted book\n'
                    for i in range(max_level):
                        item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=' + str(i) + '}] run summon item ~ ~10 ~ {Item:{id:"minecraft:enchanted_book",tag:{StoredEnchantments:[{id:"minecraft:' + entry2['item'] + '", lvl:' + str(i + 1) + 's}]},Count:1b}}\n'
                else:
                    item2 += '\n# Summon enchanted book\n'
                    item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon item ~ ~10 ~ {Item:{id:"minecraft:enchanted_book",tag:{StoredEnchantments:[{id:"minecraft:' + entry2['item'] + '", lvl:1s}]},Count:1b}}\n'
                item2 += '\n# Give fancy particle for the current team\n'
                item2 += 'execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += 'execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += 'execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += 'execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += '\n# Kill the armor stands\n'
                item2 += 'kill @e[type=minecraft:armor_stand,tag=spawner]'
                item2 += '\n\n# Do all of that again\n' + item2.replace('~10', '~12')

                item3 = '{\n'
                item3 += '"function": "minecraft:set_enchantments",\n'
                item3 += '  "enchantments": {\n'
                item3 += '    "minecraft:' + entry2['item'] + '": -255\n'
                item3 += '  }\n'
                item3 += '}'

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}.mcfunction'.format(entry2['item'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(item1)
                rb.close()

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}2.mcfunction'.format(entry2['item'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(item2)
                rb.close()

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/item_modifiers/{}.json'.format(entry2['item'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(item3)
                rb.close()

            else:
                item1 = '# Attempt to kill / clear item'
                item1 += '\nexecute store result score #items_killed vars run kill @e[type=minecraft:item,nbt={Item:{id:"minecraft:' + entry2['item'] + '"}}]'
                item1 += '\nexecute store result score #items_cleared vars run clear @a minecraft:' + entry2['item']
                item1 += '\n\n# If item not killed / cleared, summon some'
                item1 += '\nexecute if score #items_killed vars matches 0 if score #items_cleared vars matches 0 run schedule function wordsmith:detect/item/{}2 1t'.format(entry2['item'])

                item2 = '# Summon armor stands\n'
                item2 += 'scoreboard players operation #spreaded_armor_stands vars = #curr_item_spawning_density vars\n'
                item2 += 'function wordsmith:detect/spread_armor_stands_r1\n'
                item2 += '\n# Summon item\n'
                item2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + entry2['item'] + '",Count:1b}}\n'
                item2 += '\n# Give fancy particle for the current team\n'
                item2 += 'execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += 'execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += 'execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += 'execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30\n'
                item2 += '\n# Kill the armor stands\n'
                item2 += 'kill @e[type=minecraft:armor_stand,tag=spawner]'
                item2 += '\n\n# Do all of that again\n' + item2.replace('~10', '~12')

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}.mcfunction'.format(entry2['item'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(item1)
                rb.close()

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}2.mcfunction'.format(entry2['item'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(item2)
                rb.close()