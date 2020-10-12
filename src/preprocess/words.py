from src.helpers.file_dict_source import get_words_from_file


def preprocess_words(args):
    words = set()
    if args.words:
        min_len, max_len = min(args.words, key=len), max(words, key=len)
    else:
        min_len, max_len = float('inf'), 0
        for word in get_words_from_file(args.dictionary_file):
            word = word
            word_len = len(word)
            min_len, max_len = min(min_len, word_len), max(max_len, word_len)
            words.add(word)
    return words, min_len, max_len
