# 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = list(word_file.read().split())

    return valid_words