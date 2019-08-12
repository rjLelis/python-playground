
FORBIDDEN_CHARS = (".", ",", "!", ";", ":",
        "-", "_", "?", "/", "\\", "|", "*", 
        "+", "=", "@", "#", "$", "%", "^", 
        "&", "(", ")", "{", "}", "[", "]", "~", "`")

def remove_special_char(string):
    ''' Removes all special characters from a string '''
    new_string = ""
    for character in string:
        if character not in FORBIDDEN_CHARS:
            new_string += character
    return new_string


def reverse(string):
    ''' Reverses a string'''
    return string[::-1]


def is_palindrome(word):
    ''' Returns true if a word is palindrome '''
    return remove_special_char(word.lower()) == \
        reverse(remove_special_char(word.lower()))