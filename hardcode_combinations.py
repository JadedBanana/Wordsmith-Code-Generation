import itertools

possibilities = [False, True]

n = 0

for r in possibilities:
    for b in possibilities:
        for g in possibilities:
            for y in possibilities:
                stuff = []
                if r:
                    stuff.append('Red')
                if b:
                    stuff.append('Blue')
                if g:
                    stuff.append('Green')
                if y:
                    stuff.append('Yellow')

                print('{} {}'.format(n, ('r' if r else '') + ('b' if b else '') + ('g' if g else '') + ('y' if y else '')))
                n+= 1

