from words import words_en
import json
import os

words_old = words_en.words
synonyms_old = words_en.synonyms
synonyms_old = [synonyms_old[word] for word in synonyms_old]
synonyms_old2 = []
for synonym in synonyms_old:
    synonyms_old2 += synonym
synonyms_old = synonyms_old2

words_ignore = [
    'redstone_wall_torch',
    'warped_wall_sign',
    'crimson_wall_sign',
    'skeleton_wall_skull',
    'wither_skeleton_wall_skull',
    'zombie_wall_head',
    'player_wall_head',
    'creeper_wall_head',
    'dragon_wall_head',
    'tube_coral_wall_fan',
    'brain_coral_wall_fan',
    'bubble_coral_wall_fan',
    'fire_coral_wall_fan',
    'horn_coral_wall_fan',
    'dead_tube_coral_wall_fan',
    'dead_brain_coral_wall_fan',
    'dead_bubble_coral_wall_fan',
    'dead_fire_coral_wall_fan',
    'dead_horn_coral_wall_fan',
    'wall_torch',
    'soul_wall_torch',
    'oak_wall_sign',
    'spruce_wall_sign',
    'birch_wall_sign',
    'acacia_wall_sign',
    'jungle_wall_sign',
    'dark_oak_wall_sign',
    'nether_portal',
    'end_gateway',
    'end_portal',
    'set_spawn',
    'kelp_plant',
    'attached_pumpkin_stem',
    'chipped_anvil',
    'damaged_anvil',
    'repeating_command_block',
    'chain_command_block',
    'piston_head',
    'moving_piston',
    'attached_melon_stem',
    'melon_stem',
    'potted_oak_sapling',
    'potted_spruce_sapling',
    'potted_birch_sapling',
    'potted_jungle_sapling',
    'potted_acacia_sapling',
    'potted_dark_oak_sapling',
    'potted_fern',
    'potted_dandelion',
    'potted_poppy',
    'potted_blue_orchid',
    'potted_allium',
    'potted_azure_bluet',
    'potted_red_tulip',
    'potted_orange_tulip',
    'potted_white_tulip',
    'potted_pink_tulip',
    'potted_oxeye_daisy',
    'potted_cornflower',
    'potted_lily_of_the_valley',
    'potted_wither_rose',
    'potted_red_mushroom',
    'potted_brown_mushroom',
    'potted_dead_bush',
    'potted_cactus',
    'potted_bamboo',
    'potted_crimson_fungus',
    'potted_warped_fungus',
    'potted_crimson_roots',
    'potted_warped_roots',
    'void_air',
    'cave_air',
    'bubble_column',
    'creeper_banner_pattern',
    'skull_banner_pattern',
    'flower_banner_pattern',
    'mojang_banner_pattern',
    'globe_banner_pattern',
    'piglin_banner_pattern',
    'weeping_vines_plant',
    'twisting_vines_plant',
    'cocoa',
    'sign',
    'tripwire',
    'music_disc_13',
    'music_disc_cat',
    'music_disc_blocks',
    'music_disc_chirp',
    'music_disc_far',
    'music_disc_mall',
    'music_disc_mellohi',
    'music_disc_stal',
    'music_disc_strad',
    'music_disc_ward',
    'music_disc_11',
    'music_disc_wait',
    'music_disc_pigstep',
    'area_effect_cloud',
    'boat',
    'sign',
    'evoker_fangs',
    'falling_block',
    'fishing_bobber',
    'leash_knot',
    'llama_spit',
    'shulker_bullet',
    'small_fireball',
    'bamboo_sapling',
    'petrified_oak_slab',
    'pumpkin_stem',
    'light',
    'tipped_arrow',
    'marker',
]

words = {}

synonyms = {}

sets = [
    json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/resourcepacks/Default Resource Pack/assets/minecraft/lang', 'en_us.json'), 'r')),
    json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/resourcepacks/Default Resource Pack/assets/minecraft/lang', 'en_ca.json'), 'r')),
    json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/resourcepacks/Default Resource Pack/assets/minecraft/lang', 'en_nz.json'), 'r')),
    json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/resourcepacks/Default Resource Pack/assets/minecraft/lang', 'en_gb.json'), 'r')),
    json.load(open(os.path.join('C:/Users/popki/AppData/Roaming/.minecraft/resourcepacks/Default Resource Pack/assets/minecraft/lang', 'en_au.json'), 'r'))
]

for set in sets:
    for lang_name in set:
        # Formal name
        word_formal_name = set[lang_name].lower()

        # If formal name in old_words, ignore it
        if word_formal_name in words_old or word_formal_name in synonyms_old:
            continue

        # Blocks
        if lang_name.startswith('block.minecraft.'):
            word_name = lang_name[16:]
            if '.' in word_name:
                continue
            # If word_name in ignore, ignore it
            if word_name in words_ignore:
                continue
            # If word formal not in dict, first test for synonyms
            if word_formal_name not in words:
                found = False
                for existing_word in words:
                    if {'block': word_name} in words[existing_word] and existing_word[0] == word_formal_name[0] and existing_word[-1] == word_formal_name[-1]:
                        if existing_word in synonyms:
                            synonyms[existing_word].append(word_formal_name)
                        else:
                            synonyms[existing_word] = [word_formal_name]
                        found = True
                if not found:
                    words[word_formal_name] = [{'block': word_name}]
            else:
                if {'block': word_name} not in words[word_formal_name]:
                    words[word_formal_name].append({'block': word_name})

        # Entities
        if lang_name.startswith('entity.minecraft.'):
            word_name = lang_name[17:]
            if '.' in word_name:
                continue
            # If word_name in ignore, ignore it
            if word_name in words_ignore:
                continue
            # If word formal not in dict, first test for synonyms
            if word_formal_name not in words:
                for existing_word in words:
                    if {'entity': word_name} in words[existing_word] and existing_word[0] == word_formal_name[0] and existing_word[-1] == word_formal_name[-1]:
                        if existing_word in synonyms:
                            synonyms[existing_word].append(word_formal_name)
                        else:
                            synonyms[existing_word] = [word_formal_name]
                words[word_formal_name] = [{'entity': word_name}]
            else:
                if {'entity': word_name} not in words[word_formal_name]:
                    words[word_formal_name].append({'entity': word_name})

        # Items
        if lang_name.startswith('item.minecraft.'):
            word_name = lang_name[15:]
            if '.' in word_name:
                continue
            # If word_name in ignore, ignore it
            if word_name in words_ignore:
                continue
            # If word formal not in dict, first test for synonyms
            if word_formal_name not in words:
                for existing_word in words:
                    if {'item': word_name} in words[existing_word] and existing_word[0] == word_formal_name[0] and existing_word[-1] == word_formal_name[-1]:
                        if existing_word in synonyms:
                            synonyms[existing_word].append(word_formal_name)
                        else:
                            synonyms[existing_word] = [word_formal_name]
                words[word_formal_name] = [{'item': word_name}]
            else:
                if {'item': word_name} not in words[word_formal_name]:
                    words[word_formal_name].append({'item': word_name})

synonyms2 = {}
for synonym in synonyms:
    if synonyms[synonym]:
        synonyms2[synonym] = synonyms[synonym]

def print_dict(d):
    print('{')
    for key in d:
        if isinstance(d[key], str):
            print('\t\'{}\': \'{}\','.format(key, d[key]))
        else:
            print('\t\'{}\': {},'.format(key, d[key]))
    print('}')

print_dict(words)
print_dict(synonyms2)