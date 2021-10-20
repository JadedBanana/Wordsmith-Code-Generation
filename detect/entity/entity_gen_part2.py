"""
Generates all the block detection files (part 1 / deleting entities).
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each entry in the list
for entry in word_list:
    # Iterate through each DEFINITION of each word
    for entry2 in word_list[entry]:
        # Cancel if it's manual or if it's not a entity
        if 'manual' in entry2 or 'entity' not in entry2:
            continue

        # Generate full string
        full = ''
        # Custom densities are really common with entity spawning.
        if 'density' in entry2:
            # A ratio is formed.
            ratio = float(entry2['density'])
            # If the ratio isn't one, we need to add a scoreboard modifier that edits the curr_entity_spawning_density variable.
            if ratio != 1.:
                full += '# Set entity density ({}x)\n'.format(ratio)
                # Split the ratio into an integer ratio (numerator and denominator)
                ratio2 = ratio.as_integer_ratio()
                # Multiply by numerator
                if ratio2[0] != 1:
                    full += 'scoreboard players set #temp vars {}\n'.format(ratio2[0])
                    full += 'scoreboard players operation #curr_entity_spawning_density vars *= #temp vars\n'
                # Divide by denominator
                if ratio2[1] != 1:
                    full += 'scoreboard players set #temp vars {}\n'.format(ratio2[0])
                    full += 'scoreboard players operation #curr_entity_spawning_density vars /= #temp vars\n'
                # And make sure we drop at LEAST 1 entity.
                if ratio < 1:
                    full += 'execute if score #curr_entity_spawning_density vars matches 0 run scoreboard players set #curr_entity_spawning_density vars 1'
                full += '\n'
        # Summon the armor stands.
        full += '# Summon armor stands\n'
        full += 'scoreboard players operation #spreaded_armor_stands vars = #curr_entity_spawning_density vars\n'
        full += 'function wordsmith:detect/spread_armor_stands_r1\n'
        # Finally get into the dropping part!
        full += '\n# Summon entity\n'
        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon minecraft:' + entry2['entity'] + ' ~ ~' + str(2.5 if 'spawn_height' not in entry2 else entry2['spawn_height']) + ' ~' + (' ' + entry2['added_tags'] if 'added_tags' in entry2 else '') + '\n'
        # Particle appearance is complicated. It's usually hardcoded into each dictionary entry, so we have to read that.
        full += '\n# Give fancy particle for the current team\n'
        p_w = str(0.5 if 'particle' not in entry2 else entry2['particle']['w'])
        p_h = str(0.5 if 'particle' not in entry2 else entry2['particle']['h'])
        p_c = str(100 if 'particle' not in entry2 or 'c' not in entry2['particle'] else entry2['particle']['c'])
        spawn_height = str((2.5 if 'spawn_height' not in entry2 else entry2['spawn_height']) + float(p_h) * 2 - 0.25 + (0 if 'particle' not in entry2 or 'v_offset' not in entry2['particle'] else entry2['particle']['v_offset']))
        full += 'execute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~' + spawn_height + ' ~ ' + p_w + ' ' + p_h + ' ' + p_w + ' 1 ' + p_c + '\n'
        full += 'execute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~' + spawn_height + ' ~ ' + p_w + ' ' + p_h + ' ' + p_w + ' 1 ' + p_c + '\n'
        full += 'execute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~' + spawn_height + ' ~ ' + p_w + ' ' + p_h + ' ' + p_w + ' 1 ' + p_c + '\n'
        full += 'execute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~' + spawn_height + ' ~ ' + p_w + ' ' + p_h + ' ' + p_w + ' 1 ' + p_c + '\n'
        # Kill the armor stands
        full += '\n# Kill the armor stands\n'
        full += 'kill @e[type=minecraft:armor_stand,tag=spawner]'

        # Write
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/entity/{}2.mcfunction'.format(entry2['entity'].replace(' ', '_').replace('\'', '_')))