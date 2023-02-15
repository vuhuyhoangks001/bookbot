def main():
    text = get_book_text("books/frankenstein.txt")
    number_of_words = count_words(text)
    print(number_of_words)

    number_of_letters = count_letters(text)
    print(number_of_letters)

def count_words(text):
    sum = 0
    text = text.split()
    for word in text:
        sum += 1

    return sum


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    letter_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in letter_dict:
            letter_dict[lower_char] = 1
        else:
            letter_dict[lower_char] += 1

    return letter_dict


main()