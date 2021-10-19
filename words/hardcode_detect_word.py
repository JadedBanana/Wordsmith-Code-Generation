from words import words_en

word_list = words_en.words
synonym_list = words_en.synonyms

full = '# This is the function that detects all the text in books. It is thousands of lines long. It was made via automation, because no sane person would do this manually.'

for entry in word_list:
    if 'banned' in word_list[entry][0]:
        full+= '\nexecute unless score #word_submitted vars matches 1 if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + entry + '"]}}]}] run function wordsmith:detect/words/banned'
        continue
    full+= '\nexecute unless score #word_submitted vars matches 1 if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + entry + '"]}}]}] run function wordsmith:detect/words/' + entry.replace(' ', '_').replace('\'', '_')
    if entry in synonym_list:
        for s in synonym_list[entry]:
            full += '\nexecute unless score #word_submitted vars matches 1 if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + s + '"]}}]}] run function wordsmith:detect/words/' + entry.replace(' ', '_').replace('\'', '_')
full += '\n\n# If no SELF word submitted, we know word not recognized'
full += '\nexecute if score @s word_submitted matches 0 run function wordsmith:detect/detect_invalid'
full += '\n\n# If no GLOBAL word submitted, we know the entry was not accepted, so we clear the book'
full += '\nexecute unless score #word_submitted vars matches 1 unless score @s word_submitted matches 0 run clear @s minecraft:writable_book{Wordsmith:1b}'

rb = open('C:/Users/popki/AppData/Roaming/.minecraft/saves/Wordsmith/datapacks/Wordsmith/data/wordsmith/functions/detect/detect.mcfunction', 'w')
rb.write(full)
rb.close()