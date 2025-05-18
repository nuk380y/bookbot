def count_words(contents):
    # Convert full string from file into list of individual words.
    words = contents.split()
    # Initiate variable for counting the number of words.
    num_words = 0

    # Iterate over the full list and keep a running count.
    for word in words:
        num_words += 1

    # Probably should have done this more simply as:
    # `return len(words)`
    # ...but hindsight's 20/20.
    return num_words


def count_chars(contents):
    # Normalize all of the individual characters to their lowercase equivalent.
    standardized = contents.lower()
    # Initiate empty dictionary
    character_count = {}

    # Iterate over every character...
    for key in standardized:
        # ...if that character already exists in the dictionary...
        if key in character_count:
            # ...add one to the count.
            character_count[key] += 1
        else:
            # If the character is showing for the first time, count the first
            # instance.
            character_count[key] = 1

    return character_count


# Literally handed to you in the "Hint" of the "Assignment".
def sort_by_count(dict):
    return dict["num"]


def list_readable(character_count):
    # Initialize an empty list.
    list_char_count = []

    # For each key in the passed dictionary...
    for key in character_count:
        # ...initialize a new empty dictionary...
        letter = {}

        # ...and if that value is a "readable" unicode character...
        if str(key).isalpha():
            # ...add it and the respective count to a more "searchable"
            # dictionary structure...
            letter = {"char": key, "num": character_count[key]}
            # ...and add that dictionary to the list.
            list_char_count.append(letter)

    # Once the list has been populated with ONLY readable characters, then
    # pass it back.
    return list_char_count
