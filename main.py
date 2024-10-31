def main():
    print_report("books/frankenstein.txt")

def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    counter = {}
    for c in text:
        c = c.lower()
        if c not in counter:
            counter[c] = 0
        counter[c] += 1
    return counter


def print_report(book):
    print(f"--- Begin report of {book} ---")
    text = None
    with open(book, "r") as book:
        text = book.read()
    print(f"{count_words(text)} words found in the document")
    chars = count_characters(text)
    for k,v in sorted(chars.items(), key=lambda x: x[1], reverse=True):
        print(f"The '{k}' character was found {v} times")
    print(f"--- End report ---")



if __name__ == "__main__":
    main()
