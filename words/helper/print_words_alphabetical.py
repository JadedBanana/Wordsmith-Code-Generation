import words

worddict = words.words_en

wordlist = [word for word in worddict]
wordlist.sort()
for word in wordlist:
    print(word)