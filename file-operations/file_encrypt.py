import argparse
from caesar_cipher import encrypt
from file_utils import get_file_content, store_file_content

parser = argparse.ArgumentParser(description='Takes a file as argument and encrypts it')

parser.add_argument('file', metavar='file to be encrypted', type=str)
parser.add_argument('key', metavar='key to encrypt',type=int)

args = parser.parse_args()

file_content = get_file_content(args.file)

new_file = store_file_content(encrypt(file_content, args.key), 'encriptado.txt')

print(f'content stored on {new_file}')