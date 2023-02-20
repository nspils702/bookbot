with open("books/frankenstein") as f:
    file_contents = f.read()
def counter():
    char_count = dict()
    strings = file_contents.split()
    for string in strings:
        for char in string:
            if char.isalpha(): 
                char = char.lower()
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    myKeys = list(char_count.keys())
    myKeys.sort()
    sorted_dict = {i: char_count[i] for i in myKeys}
    print(sorted_dict)
counter()


This is a change