from file_utils import remove_accents


def encrypt(original_message, key):
    '''
        Encrypts a message using the caesar cypher

        :params original_message, key
        :returns encrypted_message
    '''

    alphabet = ('a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z')

    encrypted_message = ''

    if type(key) == str:
        key = alphabet.index(key) + 1

    # Encrypts the original message then stores in the return variable
    for letter in remove_accents(original_message.lower()):
        encrypted_letter = ''
        if letter not in alphabet:
            encrypted_letter = letter
        else:
            letter_index = alphabet.index(letter)
            if letter not in alphabet:
                encrypted_letter = letter
            elif letter_index + key >= len(alphabet):
                encrypted_letter = \
                    alphabet[letter_index + key - len(alphabet)]
            else:
                encrypted_letter = alphabet[letter_index + key]
        encrypted_message += encrypted_letter

    return encrypted_message