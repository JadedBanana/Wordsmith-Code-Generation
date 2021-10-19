teams = ['red', 'blue', 'green', 'yellow']
letters = ['Any', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

directory_message = '''# Direct to function with correct letter
execute if score #required_letter vars matches 0 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 1 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 2 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 3 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 4 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 5 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 6 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 7 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 0 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 0 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 0 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 0 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 0 run function wordsmith:turn/bossbar/{}_any
execute if score #required_letter vars matches 0 run function wordsmith:turn/bossbar/{}_any
'''

for i in range(len(teams)):

    directory_message = '# Direct to function with correct letter'
    for j in range(27):
        directory_message += '\nexecute if score #required_letter vars matches {} run function wordsmith:turn/bossbar/{}_{}'.format(j, teams[i], letters[j].lower())

    rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/turn/bossbar/{}_directory.mcfunction'.format(teams[i]), 'w')
    rb.write(directory_message)
    rb.close()


    for j in range(len(letters)):

        bossbar_function = '# Set bossbar title based on time'
        bossbar_function += ''
        bossbar_function += '\nexecute if score #turn_time vars matches 1..20 run bossbar set minecraft:{} name "Required Letter: {} - 1 Second Remaining"'.format(i, letters[j])
        for k in range(1, 299):
            bossbar_function += '\nexecute if score #turn_time vars matches {}..{} run bossbar set minecraft:{} name "Required Letter: {} - {} Seconds Remaining"'.format(k * 20 + 1, (k + 1) * 20, i, letters[j], k + 1)
        bossbar_function += '\nexecute if score #turn_time vars matches {}.. run bossbar set minecraft:{} name "Required Letter: {} - {} Seconds Remaining"'.format(299 * 20 + 1, i, letters[j], '300+')

        rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/turn/bossbar/{}_{}.mcfunction'.format(teams[i], letters[j].lower()), 'w')
        rb.write(bossbar_function)
        rb.close()