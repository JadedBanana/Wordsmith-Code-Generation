"""
Generates all the spectator title functions. Only one file.
"""
from util import writer
import itertools

# Establishing basic variables
possibilities = [False, True]
n = -1

# Setting up the full string
full = '''# Fix negative values
execute if score #red_players_now vars matches ..-1 run scoreboard players set #red_players_now vars 0
execute if score #blue_players_now vars matches ..-1 run scoreboard players set #blue_players_now vars 0
execute if score #yellow_players_now vars matches ..-1 run scoreboard players set #yellow_players_now vars 0
execute if score #green_players_now vars matches ..-1 run scoreboard players set #green_players_now vars 0\n
# Set the title based on permutation and people left'''

# Iterate through the combinations of teams
for r in possibilities:
    for b in possibilities:
        for g in possibilities:
            for y in possibilities:

                # Record the team combination
                stuff = []
                if r:
                    stuff.append('red')
                if b:
                    stuff.append('blue')
                if g:
                    stuff.append('green')
                if y:
                    stuff.append('yellow')

                # If no stuff (first loop), increment and repeat
                if len(stuff) == 0:
                    n+= 1
                    continue

                # If there's only one team in this combination, run the endurance mode title
                if len(stuff) == 1:
                    n += 1
                    full += '\nexecute if score #team_permutation vars matches ' + str(n) + ' run title @a[scores={deaths=1..}] actionbar {"text":"Players Remaining: ","color":"' + stuff[0] + '","extra":[{"score":{"name":"#' + stuff[0] + '_players_now","objective":"vars"}}]}'

                # Otherwise, run the normal vs. title
                else:
                    # Make the list of permutations
                    permutations = list(itertools.permutations(stuff))

                    # Iterate through each permtation, making ordered functions each time
                    for perma in permutations:
                        n += 1
                        full += '\nexecute if score #team_permutation vars matches ' + str(n) + ' run title @a[scores={deaths=1..}] actionbar '
                        if perma[0] == 'red':
                            full += '{"text":"I ","obfuscated":true,"color":"light_purple","extra":[{"text":"Red Players: ","color":"red","obfuscated":false},{"score":{"name":"#red_players_now","objective":"vars"},"color":"red","obfuscated":false,"bold":true}'
                        elif perma[0] == 'blue':
                            full += '{"text":"I ","obfuscated":true,"color":"light_purple","extra":[{"text":"Blue Players: ","color":"blue","obfuscated":false},{"score":{"name":"#blue_players_now","objective":"vars"},"color":"blue","obfuscated":false,"bold":true}'
                        elif perma[0] == 'green':
                            full += '{"text":"I ","obfuscated":true,"color":"light_purple","extra":[{"text":"Green Players: ","color":"green","obfuscated":false},{"score":{"name":"#green_players_now","objective":"vars"},"color":"green","obfuscated":false,"bold":true}'
                        elif perma[0] == 'yellow':
                            full += '{"text":"I ","obfuscated":true,"color":"light_purple","extra":[{"text":"Yellow Players: ","color":"yellow","obfuscated":false},{"score":{"name":"#yellow_players_now","objective":"vars"},"color":"yellow","obfuscated":false,"bold":true}'
                        for i in range(1, len(perma)):
                            full += ',{"text":" I "},{"text":"' + perma[i][0].upper() + perma[i][1:] + ' Players: ","color":"' + perma[i] + '","obfuscated":false},{"score":{"name":"#' + perma[i] + '_players_now","objective":"vars"},"color":"' + perma[i] + '","obfuscated":false,"bold":true}'
                        full += ',{"text":" I"}]}'

# Write the file
writer.write(full, f'datapacks/Wordsmith/data/wordsmith/functions/turn/spectator_title.mcfunction')