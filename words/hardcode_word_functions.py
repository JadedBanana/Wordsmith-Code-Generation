from words import words_en
word_list = words_en.words

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

n = 1

for entry in word_list:

    word1 = '# Set word submitted'
    word1 += '\nscoreboard players set @s word_submitted 1\n'
    word1 += '\n# Check if word enabled, set appropriate score\n'
    word1 += 'scoreboard players set #word_execution_function vars 0'
    for i in reversed(range(len(word_list[entry]))):
        if 'banned' in word_list[entry][i]:
            continue
        if 'block' in word_list[entry][i]:
            if 'overpowered' in word_list[entry][i]:
                word1 += '\nexecute if score #block_terms_enabled vars matches 1 if score #overpowered_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
            else:
                word1 += '\nexecute if score #block_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
        elif 'item' in word_list[entry][i]:
            if 'overpowered' in word_list[entry][i]:
                word1 += '\nexecute if score #item_terms_enabled vars matches 1 if score #overpowered_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
            else:
                word1 += '\nexecute if score #item_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
        elif 'entity' in word_list[entry][i]:
            if 'overpowered' in word_list[entry][i]:
                word1 += '\nexecute if score #entity_terms_enabled vars matches 1 if score #overpowered_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
            else:
                word1 += '\nexecute if score #entity_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
        elif 'world' in word_list[entry][i]:
            if 'overpowered' in word_list[entry][i]:
                word1 += '\nexecute if score #world_terms_enabled vars matches 1 if score #overpowered_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
            else:
                word1 += '\nexecute if score #world_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
        elif 'meta' in word_list[entry][i]:
            if 'overpowered' in word_list[entry][i]:
                word1 += '\nexecute if score #meta_terms_enabled vars matches 1 if score #overpowered_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
            else:
                word1+= '\nexecute if score #meta_terms_enabled vars matches 1 run scoreboard players set #word_execution_function vars ' + str(i + 1)
        elif 'group' in word_list[entry][i]:
            word1 += '\nexecute if score #blanket_terms_enabled vars matches 1 '
            if 'overpowered' in word_list[entry][i]:
                word1 += 'if score #overpowered_terms_enabled vars matches 1 '
            if 'block' in word_list[entry][i]['prereq']:
                word1 += 'if score #block_terms_enabled vars matches 1 '
            if 'item' in word_list[entry][i]['prereq']:
                word1 += 'if score #item_terms_enabled vars matches 1 '
            if 'world' in word_list[entry][i]['prereq']:
                word1 += 'if score #world_terms_enabled vars matches 1 '
            if 'entity' in word_list[entry][i]['prereq']:
                word1 += 'if score #entity_terms_enabled vars matches 1 '
            if 'meta' in word_list[entry][i]['prereq']:
                word1 += 'if score #meta_terms_enabled vars matches 1 '
            word1 += 'run scoreboard players set #word_execution_function vars ' + str(i + 1)
        else:
            print('MASSIVE ERROR, entry is ' + entry)
            exit(-1)
    word1 += '\n\n# If score not 0, run -- else do punish_word_disabled'
    word1 += '\nexecute if score #word_execution_function vars matches 1.. run function wordsmith:detect/words/' + entry.replace(' ', '_').replace('\'', '_') + '2'
    word1 += '\nexecute if score #word_execution_function vars matches 0 run function wordsmith:detect/punish_word_disabled'

    word2 = '# Check if word used\n'
    word2 += 'execute if score #{} used matches 1 run function wordsmith:detect/punish_used\n'.format(entry.replace(' ', '_').replace('\'', '_'))
    word2 += 'execute unless score #{} used matches 1 run function wordsmith:detect/words/'.format(entry.replace(' ', '_').replace('\'', '_')) + entry.replace(' ', '_').replace('\'', '_') + '3'

    word3 = '# Check if word starts with required letter or required letter is 0'
    if entry[0] == 'a':
        word3 += '\nexecute unless score #required_letter vars matches 0..1 run function wordsmith:detect/punish_wrong_letter'
        word3 += '\nexecute if score #required_letter vars matches 0..1 run function wordsmith:detect/words/' + entry.replace(' ', '_').replace('\'', '_') + '4'
    else:
        word3 += '\nexecute unless score #required_letter vars matches 0 unless score #required_letter vars matches {} run function wordsmith:detect/punish_wrong_letter'.format(letter_nums[entry[0]])
        word3 += '\nexecute if score #required_letter vars matches 0 run function wordsmith:detect/words/' + entry.replace(' ', '_').replace('\'', '_') + '4'
        word3 += '\nexecute if score #required_letter vars matches {} run function wordsmith:detect/words/'.format(letter_nums[entry[0]]) + entry.replace(' ', '_').replace('\'', '_') + '4'

    word4 = '# Check if word leads to a dead end'
    word4 += '\nexecute if score #{}_words used = #{}_words_max vars run function wordsmith:detect/punish_dead_end'.format(entry[-1], entry[-1])
    word4 += '\nexecute unless score #{}_words used = #{}_words_max vars run function wordsmith:detect/words/'.format(entry[-1], entry[-1]) + entry.replace(' ', '_').replace('\'', '_') + '5'

    word5 = '# All else passed, set scoreboard values'
    word5 += '\nscoreboard players add #{}_words used 1'.format(entry[0])
    word5 += '\nscoreboard players set #{} used 1'.format(entry.replace(' ', '_').replace('\'', '_'))
    word5 += '\nscoreboard players set #required_letter vars ' + str(letter_nums[entry[-1]])
    word5 += '\n\n# Tell players the good news!'
    word5 += '\nexecute if entity @s[team=Red] run tellraw @a {"selector":"@s","color":"red","extra":[{"text":" submitted a word: "},{"text":"' + entry + '","bold":true}]}'
    word5 += '\nexecute if entity @s[team=Blue] run tellraw @a {"selector":"@s","color":"blue","extra":[{"text":" submitted a word: "},{"text":"' + entry + '","bold":true}]}'
    word5 += '\nexecute if entity @s[team=Green] run tellraw @a {"selector":"@s","color":"green","extra":[{"text":" submitted a word: "},{"text":"' + entry + '","bold":true}]}'
    word5 += '\nexecute if entity @s[team=Yellow] run tellraw @a {"selector":"@s","color":"yellow","extra":[{"text":" submitted a word: "},{"text":"' + entry + '","bold":true}]}\n'
    word5 += '\n# Run appropriate function'
    if len(word_list[entry]) > 1:
        for i in reversed(range(len(word_list[entry]))):
            if 'block' in word_list[entry][i]:
                word5 += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/block/{}'.format(i + 1, word_list[entry][i]['block'])
            elif 'item' in word_list[entry][i]:
                word5 += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/item/{}'.format(i + 1, word_list[entry][i]['item'])
            elif 'entity' in word_list[entry][i]:
                word5 += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/entity/{}'.format(i + 1, word_list[entry][i]['entity'])
            elif 'meta' in word_list[entry][i]:
                word5 += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/meta/{}'.format(i + 1, word_list[entry][i]['meta'])
            elif 'world' in word_list[entry][i]:
                word5 += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/world/{}'.format(i + 1, word_list[entry][i]['world'])
            elif 'group' in word_list[entry][i]:
                word5 += '\nexecute if score #word_execution_function vars matches {} run function wordsmith:detect/blanket/{}'.format(i + 1, word_list[entry][i]['group'])
    else:
        if 'block' in word_list[entry][0]:
            word5 += '\nfunction wordsmith:detect/block/{}'.format(word_list[entry][i]['block'])
        elif 'item' in word_list[entry][0]:
            word5 += '\nfunction wordsmith:detect/item/{}'.format(word_list[entry][i]['item'])
        elif 'entity' in word_list[entry][0]:
            word5 += '\nfunction wordsmith:detect/entity/{}'.format(word_list[entry][i]['entity'])
        elif 'meta' in word_list[entry][0]:
            word5 += '\nfunction wordsmith:detect/meta/{}'.format(word_list[entry][i]['meta'])
        elif 'world' in word_list[entry][0]:
            word5 += '\nfunction wordsmith:detect/world/{}'.format(word_list[entry][i]['world'])
        elif 'group' in word_list[entry][0]:
            word5 += '\nfunction wordsmith:detect/blanket/{}'.format(word_list[entry][i]['group'])
    word5 += '\n\n# Run the function that ends turns'
    word5 += '\nfunction wordsmith:turn/end_turn_word_get'

    rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/words/{}.mcfunction'.format(entry.replace(' ', '_').replace('\'', '_')), 'w')
    rb.write(word1)
    rb.close()

    rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/words/{}2.mcfunction'.format(entry.replace(' ', '_').replace('\'', '_')), 'w')
    rb.write(word2)
    rb.close()

    rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/words/{}3.mcfunction'.format(entry.replace(' ', '_').replace('\'', '_')), 'w')
    rb.write(word3)
    rb.close()

    rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/words/{}4.mcfunction'.format(entry.replace(' ', '_').replace('\'', '_')), 'w')
    rb.write(word4)
    rb.close()

    rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/words/{}5.mcfunction'.format(entry.replace(' ', '_').replace('\'', '_')), 'w')
    rb.write(word5)
    rb.close()

    n += 1