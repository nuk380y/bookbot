from stats import count_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    book_file = './books/frankenstein.txt'
    book_contents = get_book_text(book_file)
    doc_words = count_words(book_contents)

    print(f"{doc_words} words found in the document")


main()
