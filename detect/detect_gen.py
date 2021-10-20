"""
Generates the ONE detect/detect.mcfunction method.
"""
from util import writer
from words.word_settings import word_file

# Setup word / synonym list
word_list = word_file.words
synonym_list = word_file.synonyms

# Create full string
full = '# This is the function that detects all the text in books. It is thousands of lines long. It was made via automation, because no sane person would do this manually.'
# Go through every entry in the word list
for entry in word_list:
    # If the word is banned, modify the code
    if 'banned' in word_list[entry][0]:
        full+= '\nexecute unless score #word_submitted vars matches 1 if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + entry + '"]}}]}] run function wordsmith:detect/words/banned'
        if entry in synonym_list:
            for s in synonym_list[entry]:
                full += '\nexecute unless score #word_submitted vars matches 1 if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + s + '"]}}]}] run function wordsmith:detect/words/banned'
    # Otherwise, direct code to appropriate word function
    else:
        full+= '\nexecute unless score #word_submitted vars matches 1 if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + entry + '"]}}]}] run function wordsmith:detect/words/' + entry.replace(' ', '_').replace('\'', '_')
        if entry in synonym_list:
            for s in synonym_list[entry]:
                full += '\nexecute unless score #word_submitted vars matches 1 if entity @s[nbt={Inventory:[{id:"minecraft:writable_book",tag:{Wordsmith:true,pages:["' + s + '"]}}]}] run function wordsmith:detect/words/' + entry.replace(' ', '_').replace('\'', '_')
# Append the preset suffix on every file
full += '\n\n# If no SELF word submitted, we know word not recognized'
full += '\nexecute if score @s word_submitted matches 0 run function wordsmith:detect/detect_invalid'
full += '\n\n# If no GLOBAL word submitted, we know the entry was not accepted, so we clear the book'
full += '\nexecute unless score #word_submitted vars matches 1 unless score @s word_submitted matches 0 run clear @s minecraft:writable_book{Wordsmith:1b}'


# Write the file
writer.write(full, f'datapacks/Wordsmith/data/wordsmith/functions/detect/detect.mcfunction')