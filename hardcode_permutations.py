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

                whatever = list(itertools.permutations(stuff))

                for l in whatever:
                    ii = ''
                    if len(l) > 0:
                        ii+= l[0]
                    for i in range(1, len(l)):
                        ii+= ', ' + l[i]
                    print('# ' + str(n) + ': {}'.format(ii))
                    n+= 1

