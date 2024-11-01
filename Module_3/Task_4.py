def single_root_words(root_word : str, *other_words):
    same_words = []
    root_word = root_word.lower()
    for word in other_words:
        cur_word = word.lower()

        if len(root_word) <= len(cur_word):
            if root_word in cur_word:
                same_words.append(word)
        else:
            if cur_word in root_word:
                same_words.append(word)


    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)