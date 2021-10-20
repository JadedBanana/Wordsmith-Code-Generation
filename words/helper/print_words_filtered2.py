from words import words_en
import os

worddict = words_en.words

for word in worddict:
    for entry in worddict[word]:
        if 'manual' in entry and 'block' in entry:
            if os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/block', entry['block'] + '.mcfunction')) and os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/block', entry['block'] + '2.mcfunction')):
                print(str(entry) + '    (DONE)')
            else:
                print(entry)