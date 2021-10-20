"""
Generates all the world detection files for times of day (part 1 / set the time!)
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
        full = '# Store the current time\n'
        full += 'execute store result score #time_query vars run time query daytime\n'
        full += '\n# If we are not within time range, set time to given value\n'
        # Simple detection of what time it is. The if/else just accounts for user error
        if entry2['endtime'] < entry2['starttime']:
            full += 'execute if score #time_query vars matches {}..{} run function wordsmith:detect/world/{}2\n'.format(entry2['endtime'], entry2['starttime'], entry2['world'])
            full += '\n# Otherwise, set it to be (roughly) the opposite\n'
            full += 'execute unless score #time_query vars matches {}..{} run time add 13000'.format(entry2['endtime'], entry2['starttime'])
        else:
            full += 'execute unless score #time_query vars matches {}..{} run function wordsmith:detect/world/{}2\n'.format(entry2['starttime'], entry2['endtime'], entry2['world'])
            full += '\n# Otherwise, set it to be (roughly) the opposite\n'
            full += 'execute if score #time_query vars matches {}..{} run time add 13000'.format(entry2['starttime'], entry2['endtime'])

        # Write.
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/world/{}.mcfunction'.format(entry2['world'].replace(' ', '_').replace('\'', '_')))