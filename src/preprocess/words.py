from src.helpers.file_dict_source import get_words_from_file


def preprocess_words(args):
    if args.words:
        input_words = sorted(args.words, key=lambda x: len(x))
        min_len, max_len = len(input_words[0]), len(input_words[-1])
        words = set(input_words)
    else:
        words = set()
        min_len, max_len = float('inf'), 0
        for word in get_words_from_file(args.dictionary_file):
            word = word
            word_len = len(word)
            if word_len < min_len:
                min_len = word_len
            if word_len > max_len:
                max_len = word_len
            words.add(word)
    return words, min_len, max_len
