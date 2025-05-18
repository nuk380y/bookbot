from stats import count_chars, count_words, list_readable, sort_by_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    book_file = "./books/frankenstein.txt"
    book_contents = get_book_text(book_file)
    doc_words = count_words(book_contents)
    doc_letters = count_chars(book_contents)

    # Manipulate compiled data
    sorted_letters = list_readable(doc_letters)
    sorted_letters.sort(reverse=True, key=sort_by_count)

    # Print report to user
    print(12 * "=", "BOOKBOT", 12 * "=")
    print(f"Analyzing book found at {book_file}...")
    print(11 * "-", "Word Count", 10 * "-")
    print(f"Found {doc_words} total words")
    print(9 * "-", "Character Count", 7 * "-")
    for dictionary in sorted_letters:
        print(f"{dictionary['char']}: {dictionary['num']}")
    print(13 * "=", "END", 15 * "=")


main()
