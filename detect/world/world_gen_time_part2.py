"""
Generates all the world detection files for times of day (part 1 / change the time!)
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each entry in the list
for entry in word_list:
    # Iterate through each DEFINITION of each word
    for entry2 in word_list[entry]:
        # Cancel if it's manual or if it's not a world entry or it's not a time
        if 'manual' in entry2 or 'world' not in entry2 or 'time' not in entry2:
            continue

        # Generate full string
        # Get the current day
        full = '# Get the current day\n'
        full += 'execute store result score #day_query vars run time query day\n'
        full += 'scoreboard players set #temp vars 8\n'
        full += 'scoreboard players operation #day_query vars %= #temp vars\n'
        # Then, set the time. Days matter because of the moon phases, so we have to check for each and every day and adjust
        full += '\n# Set the time\n'
        full += 'execute if score #day_query vars matches 0 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'])
        full += 'execute if score #day_query vars matches 0 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 24000)
        full += 'execute if score #day_query vars matches 1 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 24000)
        full += 'execute if score #day_query vars matches 1 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 48000)
        full += 'execute if score #day_query vars matches 2 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 48000)
        full += 'execute if score #day_query vars matches 2 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 72000)
        full += 'execute if score #day_query vars matches 3 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 72000)
        full += 'execute if score #day_query vars matches 3 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 96000)
        full += 'execute if score #day_query vars matches 4 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 96000)
        full += 'execute if score #day_query vars matches 4 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 120000)
        full += 'execute if score #day_query vars matches 5 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 120000)
        full += 'execute if score #day_query vars matches 5 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 144000)
        full += 'execute if score #day_query vars matches 6 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 144000)
        full += 'execute if score #day_query vars matches 6 if score #time_query vars matches {}.. run time set {}\n'.format(entry2['settime'] + 1, entry2['settime'] + 168000)
        full += 'execute if score #day_query vars matches 7 if score #time_query vars matches ..{} run time set {}\n'.format(entry2['settime'], entry2['settime'] + 168000)
        full += 'execute if score #day_query vars matches 7 if score #time_query vars matches {}.. run time set {}'.format(entry2['settime'] + 1, entry2['settime'])

        # Write.
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}2.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')))