def count_words(text):
    words = text.split()
    return words, len(words)

def count_characters(words):
    #words, num_words = count_words(text)
    character_count = {}
    for word in words:
        for char in word.lower():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count
    