from string_utils import is_palindrome


def main():
    word = input("Type a word to test if it is palindrome: ")
    if is_palindrome(word):
        print(f"The word '{word}' is palindrome")
    else:
        print(f"The word '{word}' isn't palindrome")


if __name__ == '__main__':
    main()
