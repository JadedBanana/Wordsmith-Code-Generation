"""
Generates all the block detection files (part 2 / dropping blocks).
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

        # Setup simple variables
        block_spawning_keyword = 'curr_item_spawning_density' if 'drop_as_item' in entry2 else 'curr_block_spawning_density'

        # Generate full string
        full = ''
        # For stuff that doesn't drop or drops once or has a custom density or is a double block, its density gets modified.
        if 'dont_drop' in entry2 or 'drop_once' in entry2 or 'density' in entry2 or 'double' in entry2:
            # A ratio is formed.
            ratio = 1.
            # Custom density resets the ratio.
            if 'density' in entry2:
                ratio = float(entry2['density'])
            # Not dropping doubles the ratio.
            if 'dont_drop' in entry2 or 'drop_once' in entry2 or 'double' in entry2:
                ratio *= 2
            # If the ratio isn't one, we need to add a scoreboard modifier that edits the curr_block_spawning_density variable.
            if ratio != 1.:
                full += '# Set block density ({}x)\n'.format(ratio)
                # Split the ratio into an integer ratio (numerator and denominator)
                ratio2 = ratio.as_integer_ratio()
                # Multiply by numerator
                if ratio2[0] != 1:
                    full += 'scoreboard players set #temp vars {}\n'.format(ratio2[0])
                    full += f'scoreboard players operation #{block_spawning_keyword} vars *= #temp vars\n'
                # Divide by denominator
                if ratio2[1] != 1:
                    full += 'scoreboard players set #temp vars {}\n'.format(ratio2[0])
                    full += f'scoreboard players operation #{block_spawning_keyword} vars /= #temp vars\n'
                # And make sure we drop at LEAST 1 block.
                if ratio < 1:
                    full += f'execute if score #{block_spawning_keyword} vars matches 0 run scoreboard players set #{block_spawning_keyword} vars 1'
                full += '\n'
        # Summon the armor stands.
        full += '# Summon armor stands\n'
        full += f'scoreboard players operation #spreaded_armor_stands vars = #{block_spawning_keyword} vars\n'
        full += 'function wordsmith:detect/spread_armor_stands_r1\n\n'
        # Finally get into the dropping part!
        # Dropping as an item, we spawn items and use a basic particle effect for items
        if 'drop_as_item' in entry2:
            full += '# Summon block\n'
            full += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon item ~ ~10 ~ {Item:{id:"minecraft:' + entry2['block'] + '",Count:1b}}\n'
            full += '\n# Give fancy particle for the current team'
            full += '\nexecute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30'
            full += '\nexecute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30'
            full += '\nexecute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~10 ~ 0.3 0.3 0.3 1 30'
            full += '\nexecute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~10 ~ 0.3 0.3 0.3 1 30'
        # If there's a directional tag in the entry, then we need to do a little more work.
        elif 'directional_tag' in entry2:
            # Roll RNG for each armor stand
            full += '# Get RNG roll for block orientation\n'
            full += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMin 0\n'
            # Modify max value based on the directional tag
            if entry2['directional_tag'] == 'axis':
                full += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMax 3\n'
            elif entry2['directional_tag'] == 'facing':
                full += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMax 4\n'
            elif entry2['directional_tag'] == 'facing2':
                full += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMax 5\n'
            elif entry2['directional_tag'] == 'shape':
                full += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMax 2\n'
            elif entry2['directional_tag'] == 'rotation':
                full += 'scoreboard players set @e[type=minecraft:armor_stand,tag=spawner] jrngMax 16\n'
            full += 'execute as @e[type=minecraft:armor_stand,tag=spawner] run function jrng:roll\n\n'
            # Then, summon block according to each armor stand's RNG value
            full += '# Summon block\n'
            # Don't drop
            if 'dont_drop' in entry2:
                # Axis (logs, usually)
                if entry2['directional_tag'] == 'axis':
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[axis=x' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[axis=y' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[axis=z' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                # Facing (typically chests)
                elif entry2['directional_tag'] == 'facing':
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[facing=north' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[facing=east' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[facing=south' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=3}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[facing=west' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                # Facing2 (shulkers, dispensers)
                elif entry2['directional_tag'] == 'facing2':
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[facing=north' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[facing=east' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[facing=south' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=3}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[facing=west' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=4}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[facing=up' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                # Shape (rails)
                elif entry2['directional_tag'] == 'shape':
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[shape=east_west' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[shape=north_south' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                # Rotation (banners, signs)
                elif entry2['directional_tag'] == 'rotation':
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=0' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=1' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=2' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=3}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=3' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=4}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=4' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=5}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=5' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=6}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=6' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=7}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=7' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=8}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=8' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=9}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=9' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=10}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=10' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=11}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=11' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=12}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=12' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=13}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=13' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=14}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=14' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=15}] run setblock ~ ~ ~ minecraft:' + entry2['block'] + '[rotation=15' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=').replace('{', '') + '' if 'required_tag' in entry2 else ']') + (entry2['required_nbt'] if 'required_nbt' in entry2 else '') + '\n'
                # Give the fancy particle
                full += '\n# Give fancy particle for the current team'
                full += '\nexecute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~0 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~0 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~0 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~0 ~ 0.6 0.6 0.6 1 60'
            # All that again, but with drops
            else:
                # Axis (logs, usually)
                if entry2['directional_tag'] == 'axis':
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{axis:"x"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{axis:"y"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{axis:"z"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                # Facing (typically chests)
                if entry2['directional_tag'] == 'facing':
                    # Double blocks (doors!)
                    if 'double' in entry2:
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"north",half:"lower"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run summon falling_block ~ ~11 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"north",half:"upper"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"east",half:"lower"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run summon falling_block ~ ~11 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"east",half:"upper"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"south",half:"lower"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run summon falling_block ~ ~11 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"south",half:"upper"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=3}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"west",half:"lower"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=3}] run summon falling_block ~ ~11 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"west",half:"upper"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    else:
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"north"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"east"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"south"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                        full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=3}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"west"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                # Facing2 (shulkers, dispensers)
                if entry2['directional_tag'] == 'facing2':
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"north"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"east"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"south"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=3}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"west"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=4}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{facing:"up"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                # Shape (rails)
                if entry2['directional_tag'] == 'shape':
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{shape:"east_west"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{shape:"north_south"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                # Rotation (banners, signs)
                if entry2['directional_tag'] == 'rotation':
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=0}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"0"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=1}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"1"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=2}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"2"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=3}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"3"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=4}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"4"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=5}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"5"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=6}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"6"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=7}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"7"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=8}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"8"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=9}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"9"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=10}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"10"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=11}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"11"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=12}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"12"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=13}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"13"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=14}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"14"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                    full += 'execute at @e[type=minecraft:armor_stand,tag=spawner,scores={jrngResult=15}] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + ',Properties:{rotation:"15"' + (',' + str(entry2['required_tag']).replace('{', '').replace('\'', '').replace(':', ':"').replace('}', '"}').replace(' ', '') if 'required_tag' in entry2 else '}') + '},Time:1}\n'
                # Give the fancy particle
                full += '\n# Give fancy particle for the current team'
                full += '\nexecute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~10 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~10 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~10 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~10 ~ 0.6 0.6 0.6 1 60'
        # No rotational tag, normal drop
        else:
            full += '# Summon block\n'
            # Dont drop
            if 'dont_drop' in entry2:
                full += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run setblock ~ ~ ~ minecraft:{}'.format(entry2['block']) + (str(entry2['required_tag']).replace('{', '[').replace('\'', '').replace('}', ']').replace(' ', '').replace(':', '=') + '\n' if 'required_tag' in entry2 else '\n')
                full += '\n# Give fancy particle for the current team'
                full += '\nexecute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~0 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~0 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~0 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~0 ~ 0.6 0.6 0.6 1 60'
            # Drop
            else:
                full += 'execute at @e[type=minecraft:armor_stand,tag=spawner] run summon falling_block ~ ~10 ~ {BlockState:{Name:"minecraft:' + entry2['block'] + '"' + (',Properties:' + str(entry2['required_tag']).replace('\'', '').replace(':', ':"').replace('}', '"}').replace(',', '",').replace(' ', '') if 'required_tag' in entry2 else '') + '},Time:1}\n'
                full += '\n# Give fancy particle for the current team'
                full += '\nexecute if score #team_turn vars matches 0 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 0.1 0.1 1 ~ ~10 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 1 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 0.2 1 1 ~ ~10 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 2 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 0.2 1 0.2 1 ~ ~10 ~ 0.6 0.6 0.6 1 60'
                full += '\nexecute if score #team_turn vars matches 3 at @e[type=minecraft:armor_stand,tag=spawner] run particle minecraft:dust 1 1 0.1 1 ~ ~10 ~ 0.6 0.6 0.6 1 60'
        # Kill the armor stands
        full += '\n\n# Kill the armor stands'
        full += '\nkill @e[type=minecraft:armor_stand,tag=spawner]'
        # Then do ALL OF THAT again (for most stuff), but a little higher if we dropped it.
        if not 'dont_drop' in entry2 and not 'drop_once' in entry2 and not 'double' in entry2:
            full += '\n\n# Do all of that again\n' + full.replace('~10', '~12')

        # Write.
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/block/{}2.mcfunction'.format(entry2['block'].replace(' ', '_').replace('\'', '_')))