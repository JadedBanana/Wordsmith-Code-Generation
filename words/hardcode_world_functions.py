from words import words_en
word_list = words_en.words

for entry in word_list:
    for entry2 in word_list[entry]:
        if 'manual' in entry2:
            continue
        if 'world' in entry2:

            if 'gamerule' in entry2:

                world1 = '# See if gamerule enabled\n'
                world1 += 'execute store result score #gamerule_enabled vars run gamerule doDaylightCycle\n'
                world1 += '\n# Toggle gamerule\n'
                world1 += 'execute if score #gamerule_enabled vars matches 0 run gamerule doDaylightCycle true\n'
                world1 += 'execute if score #gamerule_enabled vars matches 1 run gamerule doDaylightCycle false'

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(world1)
                rb.close()

            elif 'time' in entry2:

                world1 = '# Store the current time\n'
                world1 += 'execute store result score #time_query vars run time query daytime\n'
                world1 += '\n# If we are not within time range, set time to given value\n'
                if entry2['endtime'] < entry2['starttime']:
                    world1 += 'execute if score #time_query vars matches {}..{} run function wordsmith:detect/world/{}2\n'.format(entry2['endtime'], entry2['starttime'], entry2['world'])
                    world1 += '\n# Otherwise, set it to be (roughly) the opposite\n'
                    world1 += 'execute unless score #time_query vars matches {}..{} run time add 13000'.format(entry2['endtime'], entry2['starttime'])
                else:
                    world1 += 'execute unless score #time_query vars matches {}..{} run function wordsmith:detect/world/{}2\n'.format(entry2['starttime'], entry2['endtime'], entry2['world'])
                    world1 += '\n# Otherwise, set it to be (roughly) the opposite\n'
                    world1 += 'execute if score #time_query vars matches {}..{} run time add 13000'.format(entry2['starttime'], entry2['endtime'])

                world2 = '# Get the current day\n'
                world2 += 'execute store result score #day_query vars run time query day\n'
                world2 += 'scoreboard players set #temp vars 8\n'
                world2 += 'scoreboard players operation #day_query vars %= #temp vars\n'
                world2 += '\n# Set the time\n'
                world2 += 'execute if score #day_query vars matches 0 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'])
                world2 += 'execute if score #day_query vars matches 0 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 24000)
                world2 += 'execute if score #day_query vars matches 1 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 24000)
                world2 += 'execute if score #day_query vars matches 1 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 48000)
                world2 += 'execute if score #day_query vars matches 2 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 48000)
                world2 += 'execute if score #day_query vars matches 2 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 72000)
                world2 += 'execute if score #day_query vars matches 3 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 72000)
                world2 += 'execute if score #day_query vars matches 3 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 96000)
                world2 += 'execute if score #day_query vars matches 4 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 96000)
                world2 += 'execute if score #day_query vars matches 4 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 120000)
                world2 += 'execute if score #day_query vars matches 5 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 120000)
                world2 += 'execute if score #day_query vars matches 5 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 144000)
                world2 += 'execute if score #day_query vars matches 6 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 144000)
                world2 += 'execute if score #day_query vars matches 6 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 168000)
                world2 += 'execute if score #day_query vars matches 7 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 168000)
                world2 += 'execute if score #day_query vars matches 7 if score #time_query vars matches {}.. run time set {}'.format(entry2['settime'] + 1, entry2['settime'])

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(world1)
                rb.close()

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}2.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(world2)
                rb.close()

            elif 'moon_phase' in entry2:

                world1 = '# Get the current day\n'
                world1 += 'execute store result score #day_query vars run time query day\n'
                world1 += 'scoreboard players set #temp vars 8\n'
                world1 += 'scoreboard players operation #day_query vars %= #temp vars\n'
                world1 += '\n# If current day matches desired phase, change\n'
                world1 += 'execute if score #day_query vars matches {} run time add 4d\n'.format(entry2['moon_phase'])
                world1 += '\n# Otherwise, set to desired phase\n'
                world1 += 'execute unless score #day_query vars matches {} run function wordsmith:detect/world/{}2'.format(entry2['moon_phase'], entry2['world'])

                world2 = '# Add time to the next moon phase'
                for i in range(1, 8):
                    world2 += '\nexecute if score #day_query vars matches {} run time add {}d'.format((entry2['moon_phase'] - i) % 8, i)

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(world1)
                rb.close()

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}2.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(world2)
                rb.close()

            elif 'effect' in entry2:

                world1 = '# Detect entities with effect\n'
                world1 += 'execute store result score #effects_cleared vars run effect clear @e minecraft:' + entry2['world'] + '\n'
                world1 += '\n# If effect not cleared, give it to all players\n'
                world1 += 'execute if score #effects_cleared vars matches 0 run effect give @a[scores={deaths=0}] minecraft:' + entry2['world'] + ' 1000000 0'

                rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')), 'w')
                rb.write(world1)
                rb.close()
