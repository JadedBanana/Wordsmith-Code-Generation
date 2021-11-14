from util import path
from words.word_settings import word_file

# Setup word list
word_list = word_file.words


def remove_numbers(word):
    for i in '0123456789':
        word = word.strip(i)
    return word

done = 0
total = 0
for word in word_list:
    for entry in word_list[word]:
        if 'group' in entry and 'manual' not in entry and 'block' in entry['prereq'] and not 'one_block' in entry:
            total += 1
            if not path.isfile('datapacks/Wordsmith/data/wordsmith/tags/blocks/{}.json'.format(remove_numbers(entry['group']))):
                print(entry)
            else:
                done += 1

print(f'{done} done out of {total} total')
