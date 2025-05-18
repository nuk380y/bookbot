def count_words(contents):
    words = contents.split()
    num_words = 0

    for word in words:
        num_words += 1

    return num_words


def count_chars(contents):
    standardized = contents.lower()
    character_count = {}

    for key in standardized:
        if key in character_count:
            character_count[key] += 1
        else:
            character_count[key] = 1

    return character_count


def sort_by_count(dict):
    return dict["num"]


def list_readable(character_count):
    list_char_count = []

    for key in character_count:
        letter = {}

        if str(key).isalpha():
            letter = {"char": key, "num": character_count[key]}
            list_char_count.append(letter)

    return list_char_count
