def remove_special_char(string):
    ''' Removes all special characters from a string '''
    forbidden_char = (".", ",", "!", ";", ":", "-", "_", "?", "/")
    new_string = ""
    for s in string:
        if s not in forbidden_char:
            new_string += s
    return new_string


def reverse(string):
    ''' Reverses a string'''
    return string[::-1]


def palindrome_test(word):
    ''' Returns true if a word is palindrome '''
    return remove_special_char(word.lower()) == \
        reverse(remove_special_char(word.lower()))


def main():
    word = input("Type a word to test if it is palindrome: ")
    is_palindrome = palindrome_test(word)
    if is_palindrome:
        print(f"The word '{word}' is palindrome")
    else:
        print(f"The word '{word}' isn't palindrome")


if __name__ == '__main__':
    main()
