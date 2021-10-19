import os

files = os.listdir('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks')

for fil in files:
    if fil.endswith('3.mcfunction'):
        m = open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks', fil), 'r')
        sti = m.read().split('\n')
        print(sti)