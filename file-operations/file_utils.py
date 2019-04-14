from unidecode import unidecode


def remove_accents(string):
    return unidecode(string)

def get_file_content(file):
    with open(file, 'r') as f:
        file_string = f.read()
    return file_string


def store_file_content(content, file='new_file.txt'):
    with open(file, 'w') as f:
        f.write(content)
    return f'content stored on {file}'
