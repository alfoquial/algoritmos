def check_anagram(word_1, word_2):
    """Check if two words are anagrams"""
    are_anagram = True
    list_word_2 = list(word_2)
    if len(word_1) != len(word_2):
        are_anagram = False
    else:
        for letter in word_1:
            if letter not in list_word_2:
                are_anagram = False
            else:
                list_word_2.remove(letter)
    return are_anagram

