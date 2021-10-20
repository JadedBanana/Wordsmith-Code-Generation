"""
Generates all the word detection files (part 5 / setting scoreboard values and running the appropriate function).
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Set up letter numbers
letter_numbers = ' abcdefghijklmnopqrstuvwxyz'

# Iterate through each word in the word list
for entry in word_list:

    # Generate full string
    # Set scoreboard values
    full = '# All else passed, set scoreboard values'
    full += '\nscoreboard players add #{}_words used 1'.format(entry[0])
    full += '\nscoreboard players set #{} used 1'.format(entry.replace(' ', '_').replace('\'', '_'))
    full += '\nscoreboard players set #required_letter vars ' + str(letter_numbers.find(entry[-1]))
    # Send message in chat
    full += '\n\n# Tell players the good news!'
    full += '\nexecute if entity @s[team=Red] run tellraw @a {"selector":"@s","color":"red","extra":[{"text":" submitted a word: "},{"text":"' + entry + '","bold":true}]}'
    full += '\nexecute if entity @s[team=Blue] run tellraw @a {"selector":"@s","color":"blue","extra":[{"text":" submitted a word: "},{"text":"' + entry + '","bold":true}]}'
    full += '\nexecute if entity @s[team=Green] run tellraw @a {"selector":"@s","color":"green","extra":[{"text":" submitted a word: "},{"text":"' + entry + '","bold":true}]}'
    full += '\nexecute if entity @s[team=Yellow] run tellraw @a {"selector":"@s","color":"yellow","extra":[{"text":" submitted a word: "},{"text":"' + entry + '","bold":true}]}\n'
    # Run appropriate function
    full += '\n# Run appropriate function'
    # If there's more than one appropriate function, make sure we run the correct one
    if len(word_list[entry]) > 1:
        for i in reversed(range(len(word_list[entry]))):
            # Block
            if 'block' in word_list[entry][i]:
                full += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/block/{}'.format(i + 1, word_list[entry][i]['block'])
            # Item
            elif 'item' in word_list[entry][i]:
                full += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/item/{}'.format(i + 1, word_list[entry][i]['item'])
            # Entity
            elif 'entity' in word_list[entry][i]:
                full += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/entity/{}'.format(i + 1, word_list[entry][i]['entity'])
            # Meta
            elif 'meta' in word_list[entry][i]:
                full += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/meta/{}'.format(i + 1, word_list[entry][i]['meta'])
            # World
            elif 'world' in word_list[entry][i]:
                full += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/world/{}'.format(i + 1, word_list[entry][i]['world'])
            # Blanket (group)
            elif 'group' in word_list[entry][i]:
                full += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/blanket/{}'.format(i + 1, word_list[entry][i]['group'])
    # Only one function, we don't need to check which one we're running
    else:
        # Block
        if 'block' in word_list[entry][0]:
            full += '\nfunction wordsmith:detect/block/{}'.format(word_list[entry][i]['block'])
        # Item
        elif 'item' in word_list[entry][0]:
            full += '\nfunction wordsmith:detect/item/{}'.format(word_list[entry][i]['item'])
        # Entity
        elif 'entity' in word_list[entry][0]:
            full += '\nfunction wordsmith:detect/entity/{}'.format(word_list[entry][i]['entity'])
        # Meta
        elif 'meta' in word_list[entry][0]:
            full += '\nfunction wordsmith:detect/meta/{}'.format(word_list[entry][i]['meta'])
        # World
        elif 'world' in word_list[entry][0]:
            full += '\nfunction wordsmith:detect/world/{}'.format(word_list[entry][i]['world'])
        # Blanket (group)
        elif 'group' in word_list[entry][0]:
            full += '\nfunction wordsmith:detect/blanket/{}'.format(word_list[entry][i]['group'])
    # End the turn.
    full += '\n\n# Run the function that ends turns'
    full += '\nfunction wordsmith:turn/end_turn_word_get'
    
    # Write
    writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/words/{}4.mcfunction'.format(entry.replace(' ', '_').replace('\'', '_')))