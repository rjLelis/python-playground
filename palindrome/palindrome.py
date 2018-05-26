def remove_special_char(string):
    ''' Removes all special characters from a string '''
    forbidden = (".", ",", "!", ";", ":", "-", "_", "?", "/")
    new_string = ""
    for s in string:
        if s not in forbidden:
            new_string += s
    return new_string


def reverse(string):
    ''' Reverses a string'''
    return string[::-1]


def palindrome_test(word):
    ''' Returns true if a word is palindrome '''
    return remove_special_char(word) == reverse(remove_special_char(word))


def main():
    test = palindrome_test(input("Type a word to test if it is palindrome: "))
    if test:
        print(f"The word is palindrome")
    else:
        print(f"The word isn't palindrome")


if __name__ == '__main__':
    main()
