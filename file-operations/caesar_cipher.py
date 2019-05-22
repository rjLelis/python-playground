from file_utils import remove_accents


ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z')


def encrypt(original_message, key):
    '''
        Encrypts a message using the caesar cypher
        :params original_message, key
        :returns encrypted_message
    '''

    encrypted_message = ''

    if type(key) == str:
        key = ALPHABET.index(key) + 1

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
        key = ALPHABET.index(key) + 1

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