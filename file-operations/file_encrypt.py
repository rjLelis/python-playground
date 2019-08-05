import argparse
import caesar_cipher
from file_utils import get_file_content, store_file_content

def main():

    parser = argparse.ArgumentParser(description='Takes a file as argument and encrypts it')

    parser.add_argument('file', metavar='file to be encrypted', type=str)
    parser.add_argument('key', metavar='key to encrypt',type=int)
    parser.add_argument('mode', metavar='Select the mode (encrypt, decrypt)', type=str)

    args = parser.parse_args()

    try:
        eval(args.mode)(args.file, args.key)

    except NameError:
        print(f'The mode {args.mode} does not exists')


def encrypt(file, key):

    try:
        file_content = get_file_content(file)

        if file_content:
            new_file = store_file_content(caesar_cipher.encrypt(file_content, key), 'encriptado.txt')
            print(f'content stored on {new_file}')

        else:
            print(f'The file {file} is empty')

    except FileNotFoundError:
        print(f'The file {file} does not exists')
    except ValueError:
        print('The selected key does not exists in the alphabet')
    


def decrypt(file, key):
    try:
        file_content = get_file_content(file)

        if file_content:
            new_file = store_file_content(caesar_cipher.decrypt(file_content, key), 'decripted.txt')
            print(f'Content stored on {new_file}')

        else:
            print(f'The file {file} is empty')

    except FileNotFoundError:
        print(f'The file {file} does not exists')
    except ValueError:
        print('The selected key does not exists in the alphabet')


if __name__ == "__main__":
    main()