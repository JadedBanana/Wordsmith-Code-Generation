"""
Generates all the turn/bossbar functions.
One per team and letter.
"""
from util import writer

# List of all teams and letters
teams = ['red', 'blue', 'green', 'yellow']
letters = ['Any', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Iterates through teams
for i in range(len(teams)):

    # The hardcoded directory message (detects current letter and forwards to the appropriate bossbar function)
    directory_message = '# Direct to function with correct letter'
    for j in range(27):
        directory_message += '\nexecute if score #required_letter vars matches {} run function wordsmith:turn/bossbar/{}_{}'.format(j, teams[i], letters[j].lower())

    # Writes directory file
    writer.write(directory_message, f'datapacks/Wordsmith/data/wordsmith/functions/turn/bossbar/{teams[i]}_directory.mcfunction')

    # Generates per-letter bossbar files
    for j in range(len(letters)):
        bossbar_function = '# Set bossbar title based on time\n'
        # For 1 second, make sure that's not got an s at the end
        bossbar_function += '\nexecute if score #turn_time vars matches 1..20 run bossbar set minecraft:{} name "Required Letter: {} - 1 Second Remaining"'.format(i, letters[j])
        # For all seconds between 1 and 299, create a detection algorithm based on the amount of ticks
        for k in range(1, 299):
            bossbar_function += '\nexecute if score #turn_time vars matches {}..{} run bossbar set minecraft:{} name "Required Letter: {} - {} Seconds Remaining"'.format(k * 20 + 1, (k + 1) * 20, i, letters[j], k + 1)
        # For 300+ seconds, hardcode
        bossbar_function += '\nexecute if score #turn_time vars matches {}.. run bossbar set minecraft:{} name "Required Letter: {} - {} Seconds Remaining"'.format(299 * 20 + 1, i, letters[j], '300+')

        # Writes per-letter bossbar file
        writer.write(bossbar_function, f'datapacks/Wordsmith/data/wordsmith/functions/turn/bossbar/{teams[i]}_{letters[j].lower()}.mcfunction')