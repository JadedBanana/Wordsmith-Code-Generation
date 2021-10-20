"""
Generates all the word detection files (part 1 / checking if enabled, decide which type to call).
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each word in the word list
for entry in word_list:

    # Generate full string
    full = '# Set word submitted'
    full += '\nscoreboard players set @s word_submitted 1\n'
    full += '\n# Check if word enabled, set appropriate score\n'
    full += 'scoreboard players set #word_execution_function vars 0'
    # Go through the list (reversed, to set priority) and designate functions
    for i in reversed(range(len(word_list[entry]))):
        # If the entry is banned, continue
        if 'banned' in word_list[entry][i]:
            continue
        # Block
        if 'block' in word_list[entry][i]:
            if 'overpowered' in word_list[entry][i]:
                full += '\nexecute if score #block_terms_enabled vars matches 1 if score #overpowered_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
            else:
                full += '\nexecute if score #block_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
        # Item
        elif 'item' in word_list[entry][i]:
            if 'overpowered' in word_list[entry][i]:
                full += '\nexecute if score #item_terms_enabled vars matches 1 if score #overpowered_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
            else:
                full += '\nexecute if score #item_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
        # Entity
        elif 'entity' in word_list[entry][i]:
            if 'overpowered' in word_list[entry][i]:
                full += '\nexecute if score #entity_terms_enabled vars matches 1 if score #overpowered_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
            else:
                full += '\nexecute if score #entity_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
        # World
        elif 'world' in word_list[entry][i]:
            if 'overpowered' in word_list[entry][i]:
                full += '\nexecute if score #world_terms_enabled vars matches 1 if score #overpowered_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
            else:
                full += '\nexecute if score #world_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
        # Meta
        elif 'meta' in word_list[entry][i]:
            if 'overpowered' in word_list[entry][i]:
                full += '\nexecute if score #meta_terms_enabled vars matches 1 if score #overpowered_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
            else:
                full+= '\nexecute if score #meta_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
        # Blanket (group)
        elif 'group' in word_list[entry][i]:
            full += '\nexecute if score #blanket_terms_enabled vars matches 1 '
            # Since blanket prerequisites vary, add on bits of the string to check each prerequisite
            if 'overpowered' in word_list[entry][i]:
                full += 'if score #overpowered_terms_enabled vars matches 1 '
            if 'block' in word_list[entry][i]['prereq']:
                full += 'if score #block_terms_enabled vars matches 1 '
            if 'item' in word_list[entry][i]['prereq']:
                full += 'if score #item_terms_enabled vars matches 1 '
            if 'world' in word_list[entry][i]['prereq']:
                full += 'if score #world_terms_enabled vars matches 1 '
            if 'entity' in word_list[entry][i]['prereq']:
                full += 'if score #entity_terms_enabled vars matches 1 '
            if 'meta' in word_list[entry][i]['prereq']:
                full += 'if score #meta_terms_enabled vars matches 1 '
            full += 'run scoreboard players set #word_execution_function vars ' + str(i + 1)
        # Massive error, print
        else:
            print('MASSIVE ERROR, entry is ' + entry)
            exit(-1)
    # Hardcoded part where we run the next segment OR punish the player for submitting a disabled word
    full += '\n\n# If score not 0, run -- else do punish_word_disabled'
    full += '\nexecute if score #word_execution_function vars matches 1.. run function wordsmith:detect/words/' + entry.replace(' ', '_').replace('\'', '_') + '2'
    full += '\nexecute if score #word_execution_function vars matches 0 run function wordsmith:detect/punish_word_disabled'

    # Write
    writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/words/{}.mcfunction'.format(entry.replace(' ', '_').replace('\'', '_')))