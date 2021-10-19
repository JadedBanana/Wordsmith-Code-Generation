import words
word_list = words.words_en

for entry in word_list:
    for entry2 in word_list[entry]:
        if 'manual' in entry2:
            continue
        if 'entity' in entry2:

            entity1 = '# Attempt to kill mob\n'
            entity1 += 'execute store result score #entities_killed vars run tp @e[type=minecraft:' + entry2['entity'] + ',distance=..300] ~ -500 ~\n'
            entity1 += '\n# If mob not killed, summon some\n'
            entity1 += 'scoreboard players operation #curr_entity_spawning_density vars = #entity_spawning_density vars\n'
            entity1 += 'execute if score #entities_killed vars matches 0 run schedule function wordsmith:detect/entity/' + entry2['entity'] + '2 1t'

            entity2 = ''
            if 'density' in entry2:
                ratio = float(entry2['density'])
                if ratio != 1.:
                    entity2 += '# Set entity density ({}x)\n'.format(ratio)
                    ratio2 = ratio.as_integer_ratio()
                    if ratio2[0] != 1:
                        entity2 += 'scoreboard players set #temp vars {}\n'.format(ratio2[0])
                        entity2 += 'scoreboard players operation #curr_entity_spawning_density vars *= #temp vars\n'
                    if ratio2[1] != 1:
                        entity2 += 'scoreboard players set #temp vars {}\n'.format(ratio2[0])
                        entity2 += 'scoreboard players operation #curr_entity_spawning_density vars /= #temp vars\n'
                    if ratio < 1:
                        entity2 += 'execute if score #curr_entity_spawning_density vars matches 0 run scoreboard players set #curr_entity_spawning_density vars 1'
                    entity2 += '\n'
            entity2 += '# Summon armor stands\n'
            entity2 += 'scoreboard players operation #spreaded_armor_stands vars = #curr_entity_spawning_density vars\n'
            entity2 += 'function wordsmith:detect/spread_armor_stands_r1\n'
            entity2 += '\n# Summon entity\n'
            entity2 += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon minecraft:' + entry2['entity'] + ' ~ ~' + str(2.5 if 'spawn_height' not in entry2 else entry2['spawn_height']) + ' ~' + (' ' + entry2['added_tags'] if 'added_tags' in entry2 else '') + '\n'
            entity2 += '\n# Give fancy particle for the current team\n'
            p_w = str(0.5 if 'particle' not in entry2 else entry2['particle']['w'])
            p_h = str(0.5 if 'particle' not in entry2 else entry2['particle']['h'])
            p_c = str(100 if 'particle' not in entry2 or 'c' not in entry2['particle'] else entry2['particle']['c'])
            spawn_height = str((2.5 if 'spawn_height' not in entry2 else entry2['spawn_height']) + float(p_h) * 2 - 0.25 + (0 if 'particle' not in entry2 or 'v_offset' not in entry2['particle'] else entry2['particle']['v_offset']))
            entity2 += 'execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~' + spawn_height + ' ~ ' + p_w + ' ' + p_h + ' ' + p_w + ' 1 ' + p_c + '\n'
            entity2 += 'execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~' + spawn_height + ' ~ ' + p_w + ' ' + p_h + ' ' + p_w + ' 1 ' + p_c + '\n'
            entity2 += 'execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~' + spawn_height + ' ~ ' + p_w + ' ' + p_h + ' ' + p_w + ' 1 ' + p_c + '\n'
            entity2 += 'execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~' + spawn_height + ' ~ ' + p_w + ' ' + p_h + ' ' + p_w + ' 1 ' + p_c + '\n'
            entity2 += '\n# Kill the armor stands\n'
            entity2 += 'kill @e[type=minecraft:armor_stand,tag=spawner]'

            rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/entity/{}.mcfunction'.format(entry2['entity']), 'w')
            rb.write(entity1)
            rb.close()

            rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/entity/{}2.mcfunction'.format(entry2['entity']), 'w')
            rb.write(entity2)
            rb.close()