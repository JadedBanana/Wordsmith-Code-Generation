import itertools
import os

possibilities = [False, True]

n = -1

full = '''# Set title times
title @s times 0 999999999 0

# Set the title based on permutation and people left'''

for r in possibilities:
    for b in possibilities:
        for g in possibilities:
            for y in possibilities:
                stuff = []
                if r:
                    stuff.append('red')
                if b:
                    stuff.append('blue')
                if g:
                    stuff.append('green')
                if y:
                    stuff.append('yellow')

                if len(stuff) == 0:
                    n+= 1
                    continue

                whatever = list(itertools.permutations(stuff))

                if len(stuff) == 1:
                    n += 1
                    full += '\nexecute if score #team_permutation vars matches ' + str(n) + ' run title @a[scores={deaths=1..}] actionbar {"text":"Players Remaining: ","color":"' + stuff[0] + '","extra":[{"score":{"name":"#' + stuff[0] + '_players_now","objective":"vars"}}]}'

                else:

                    for l in whatever:
                        n += 1
                        full += '\nexecute if score #team_permutation vars matches ' + str(n) + ' run title @a[scores={deaths=1..}] actionbar '
                        if l[0] == 'red':
                            full += '{"text":"I ","obfuscated":true,"color":"light_purple","extra":[{"text":"Red Players: ","color":"red","obfuscated":false},{"score":{"name":"#red_players_now","objective":"vars"},"color":"red","obfuscated":false,"bold":true}'
                        elif l[0] == 'blue':
                            full += '{"text":"I ","obfuscated":true,"color":"light_purple","extra":[{"text":"Blue Players: ","color":"blue","obfuscated":false},{"score":{"name":"#blue_players_now","objective":"vars"},"color":"blue","obfuscated":false,"bold":true}'
                        elif l[0] == 'green':
                            full += '{"text":"I ","obfuscated":true,"color":"light_purple","extra":[{"text":"Green Players: ","color":"green","obfuscated":false},{"score":{"name":"#green_players_now","objective":"vars"},"color":"green","obfuscated":false,"bold":true}'
                        elif l[0] == 'yellow':
                            full += '{"text":"I ","obfuscated":true,"color":"light_purple","extra":[{"text":"Yellow Players: ","color":"yellow","obfuscated":false},{"score":{"name":"#yellow_players_now","objective":"vars"},"color":"yellow","obfuscated":false,"bold":true}'
                        for i in range(1, len(l)):
                            full += ',{"text":" I "},{"text":"' + l[i][0].upper() + l[i][1:] + ' Players: ","color":"' + l[i] + '","obfuscated":false},{"score":{"name":"#' + l[i] + '_players_now","objective":"vars"},"color":"' + l[i] + '","obfuscated":false,"bold":true}'
                        full += ',{"text":" I"}]}'

print(full)