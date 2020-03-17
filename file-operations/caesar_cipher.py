from file_utils import remove_accents
import string


ALPHABET = [letter for letter in string.ascii_lowercase]


def encrypt(original_message, key):
    '''
        Encrypts a message using the caesar cypher
        :params original_message, key
        :returns encrypted_message
    '''

    encrypted_message = ''

    if type(key) == str:
        try:
            key = ALPHABET.index(key) + 1

        except ValueError:
            raise ValueError()

    # Encrypts the original message then stores in the return variable
    for letter in remove_accents(original_message.lower()):
        if letter in ALPHABET:
            index = ALPHABET.index(letter)
            index += key

            if index >= len(ALPHABET):
                index -= len(ALPHABET)

            encrypted_message += ALPHABET[index]
        else:
            encrypted_message += letter

    return encrypted_message


def decrypt(encrypted_message, key):

    '''
        Decrypts a message using the caesar cypher
        :params encrypted_message, key
        :returns translated
    '''

    translated = ''

    if type(key) == str:
        try:
            key = ALPHABET.index(key) + 1

        except ValueError:
            raise ValueError()

    for letter in remove_accents(encrypted_message.lower()):
        if letter in ALPHABET:
            index = ALPHABET.index(letter)
            index -= key

            if index < 0:
                index += len(ALPHABET)

            translated += ALPHABET[index]

        else:
            translated += letter

    return translated
