possibilities = [0, 1, 2]
n = 0

for r in possibilities:
    for b in possibilities:
        for g in possibilities:
            for y in possibilities:
                stuff = []
                if r:
                    stuff.append('r{}'.format(r))
                if b:
                    stuff.append('b{}'.format(b))
                if g:
                    stuff.append('g{}'.format(g))
                if y:
                    stuff.append('y{}'.format(y))

                line = 'execute if score #subtitle_combination vars matches {} '.format(n)
                n+= 1

                if len(stuff) == 0:
                    line += 'run title @a subtitle {"text":"No One","color":"white","extra":[{"text":" vs... ","color":"gray"},{"text":"No One?","color":"white"}]}'
                elif len(stuff) == 1:
                    color = 'red' if 'r' in stuff[0] else ('blue' if 'b' in stuff[0] else ('green' if 'g' in stuff[0] else 'yellow'))
                    line += 'run title @a subtitle {"text":"ENDURANCE MODE","color":"' + color + '"}'
                else:
                    team = 'Red' if 'r' in stuff[0] else ('Blue' if 'b' in stuff[0] else ('Green' if 'g' in stuff[0] else 'Yellow'))
                    line += 'run title @a subtitle {' + ('"selector":"@r[team={}]'.format(team) if '1' in stuff[0] else '"text":"{} Team'.format(team)) + '","color":"' + team.lower() + '","extra":[{"text": " vs ","color":"white"}'
                    for i in range(1, len(stuff) - 1):
                        team = 'Red' if 'r' in stuff[i] else ('Blue' if 'b' in stuff[i] else ('Green' if 'g' in stuff[i] else 'Yellow'))
                        line += ',{' + ('"selector":"@r[team={}]'.format(team) if '1' in stuff[i] else '"text":"{} Team'.format(team)) + '","color":"' + team.lower() + '"},{"text": " vs ","color":"white"}'
                    team = 'Red' if 'r' in stuff[-1] else ('Blue' if 'b' in stuff[-1] else ('Green' if 'g' in stuff[-1] else 'Yellow'))
                    line += ',{' + ('"selector":"@r[team={}]'.format(team) if '1' in stuff[-1] else '"text":"{} Team'.format(team)) + '","color":"' + team.lower() + '"}]}'
                print(line)