import os

for fil in os.listdir('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks'):
    if fil.endswith('1.mcfunction'):
        os.remove(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blocks', fil))