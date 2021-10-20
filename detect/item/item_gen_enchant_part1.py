"""
Generates all the item detection files for enchants (part 1 / deleting items + clearing enchants).
"""
from util import writer
from words.word_settings import word_file

# Setup word list
word_list = word_file.words

# Iterate through each entry in the list
for entry in word_list:
    # Iterate through each DEFINITION of each word
    for entry2 in word_list[entry]:
        # Cancel if it's manual or if it's not a item or it's not an enchant
        if 'manual' in entry2 or 'item' not in entry2 or 'enchant' not in entry2:
            continue

        # Generate full string
        # This first part is pretty self-explanatory, you can read it yourself
        full = '# Set scoreboard value\n'
        full += 'scoreboard players set #enchant_removed_inv_item vars 0\n'
        full += '\n# Kill enchanted book items\n'
        full += 'execute store result score #enchant_removed_book vars run kill @e[type=item,nbt={Item:{id:"minecraft:enchanted_book",tag:{StoredEnchantments:[{"id":"minecraft:' + entry2['item'] + '"}]}}}]\n'
        full += '\n# Get rid of enchants from enchanted normal items\n'
        full += 'execute store result score #enchant_removed_item vars as @e[type=item] run data remove entity @s Item.tag.Enchantments[{id:"minecraft:' + entry2['item'] + '"}]\n'
        full += '\n# Clear enchanted book items in player inventories\n'
        full += 'execute store result score #enchant_removed_inv_book vars run clear @a minecraft:enchanted_book{StoredEnchantments:[{"id":"minecraft:' + entry2['item'] + '"}]}\n'
        full += '\n# Get rid of enchants from enchanted items in player inventories\n'
        full += 'execute if entity @a[nbt={Inventory:[{tag:{Enchantments:[{id:"minecraft:' + entry2['item'] + '"}]}}]}] run scoreboard players set #enchant_removed_inv_item vars 1\n'
        # Modification methods (automatically remove enchants from each and every item in the inventory (thank you mojang for makign this easier FUCK))
        full += 'item modify entity @a hotbar.0 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a hotbar.1 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a hotbar.2 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a hotbar.3 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a hotbar.4 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a hotbar.5 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a hotbar.6 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a hotbar.7 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a hotbar.8 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a hotbar.0 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.0 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.1 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.2 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.3 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.4 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.5 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.6 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.7 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.8 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.9 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.10 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.11 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.12 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.13 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.14 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.15 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.16 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.17 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.18 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.19 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.20 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.21 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.22 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.23 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.24 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.25 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a inventory.26 wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a armor.head wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a armor.chest wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a armor.legs wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a armor.feet wordsmith:' + entry2['item'] + '\n'
        full += 'item modify entity @a weapon.offhand wordsmith:' + entry2['item'] + '\n'
        full += '\n# Schedule next'
        full += '\nexecute if score #enchant_removed_book vars matches 0 if score #enchant_removed_item vars matches 0 if score #enchant_removed_inv_book vars matches 0 if score #enchant_removed_inv_item vars matches 0 run schedule function wordsmith:detect/item/' + entry2['item'] + '2 1t'

        # Write
        writer.write(full, 'datapacks/Wordsmith/data/wordsmith/functions/detect/item/{}.mcfunction'.format(entry2['item'].replace(' ', '_').replace('\'', '_')))