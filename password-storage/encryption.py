
def caesar_cypher(message, key):
    '''Encrypts a message using the caesar cypher [WIP]'''

    alphabet = ('a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' ,'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    encrypted = ''

    for m in message:
        if m.lower() not in alphabet:
            encrypted += m
        encrypted += alphabet[alphabet.index(m) + key]

    return encrypted


print(caesar_cypher('renato', 1))