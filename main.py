book_path = "books/frankenstein"

def main():
    file_contents = file_reader(book_path)
    char_dict = to_char_dict(file_contents)
    sorted_dict = special_sort(char_dict)
    wc = word_count(file_contents)

    print("This is a book report on Frankenstein")
    print(f"There were {wc} words in this book")
    for char in sorted_dict:
        print(f"The letter {char} was found {sorted_dict[char]} times")


def file_reader(bp):
    with open(bp) as book:
        return book.read()

def word_count(f):
    file = f.split()
    return len(file)

def to_char_dict(file):
    char_dict = dict()
    for char in file:
        if not char.isalpha():
            continue
        else:
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def special_sort(cd):
    myKeys = list(cd.keys())
    myKeys.sort()
    return {i: cd[i] for i in myKeys}

main()