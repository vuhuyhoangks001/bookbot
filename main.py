def main():
    text = get_book_text("books/frankenstein.txt")
    number_of_words = count_words(text)
    number_of_letters = count_letters(text)
    report = report_begin.format(number_of_words) + count_dict_report(number_of_letters) + report_end
    print(report)

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

report_begin = """
--- Begin report of books/frankenstein.txt ---
{0} words found in the document

"""

report_end = """
--- End report ---
"""

def count_dict_report(dict):
    result = ""
    sorted_dict_list = sorted(dict.items(), key= lambda x:x[1], reverse=True)

    for tupl in sorted_dict_list:
        if tupl[0].isalpha():
            line_report = f"The '{tupl[0]}' character was found {tupl[1]} times"
            result += line_report + "\n"

    return result

main()