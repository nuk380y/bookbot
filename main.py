import sys

from stats import count_chars, count_words, list_readable, sort_by_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def check_args():
    # Only continue if one argument is passed after the `*.py` script.
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        return filename


def main():
    # Check for two arguments and read in the second one.
    book_file = check_args()
    # Copy contents of file to malliable string value.
    book_contents = get_book_text(book_file)
    # Split into individual words and return word count.
    doc_words = count_words(book_contents)
    # Split into individual letters and return usage count of unique character
    # values.
    doc_letters = count_chars(book_contents)

    # Return list of "readable" characters and their respective count.
    sorted_letters = list_readable(doc_letters)
    # Sort list of "readable" characters.
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
