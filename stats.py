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
