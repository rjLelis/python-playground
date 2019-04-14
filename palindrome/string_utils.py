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


def is_palindrome(word):
    ''' Returns true if a word is palindrome '''
    return remove_special_char(word.lower()) == \
        reverse(remove_special_char(word.lower()))