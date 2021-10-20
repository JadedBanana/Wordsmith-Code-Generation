from words import words_en
import os

worddict = words_en.words

def remove_numbers(word):
    for i in '0123456789':
        word = word.strip(i)
    return word

for word in worddict:
    for entry in worddict[word]:
        if 'group' in entry:
            if os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blanket', entry['group'] + '.mcfunction')):
                continue
            block = 'block' in entry['prereq'] and os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blanket/block', remove_numbers(entry['group']) + '.mcfunction'))
            item = 'item' in entry['prereq'] and os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blanket/item', remove_numbers(entry['group']) + '.mcfunction'))
            entity = 'entity' in entry['prereq'] and os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blanket/entity', remove_numbers(entry['group']) + '.mcfunction'))
            world = 'world' in entry['prereq'] and os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/blanket/world', remove_numbers(entry['group']) + '.mcfunction'))
            print(str(entry) + (' (BLOCK DONE)' if block else '') + (' (ITEM DONE)' if item else '') + (' (ENTITY DONE)' if entity else '') + (' (WORLD DONE)' if world else ''))
        if 'block' in entry and not os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/block', entry['block'] + '.mcfunction')):
            print(entry)
        if 'item' in entry and not os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/item', entry['item'] + '.mcfunction')):
            print(entry)
        if 'entity' in entry and not os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/entity', entry['entity'] + '.mcfunction')):
            print(entry)
        if 'world' in entry and not os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/world', entry['world'] + '.mcfunction')):
            print(entry)
        if 'meta' in entry and not os.path.isfile(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/meta', entry['meta'] + '.mcfunction')):
            print(entry)
            break