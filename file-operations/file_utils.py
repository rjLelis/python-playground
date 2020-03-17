from unidecode import unidecode


def remove_accents(string):
    return unidecode(string)

def get_file_content(file):
    file_extention = get_file_extention(file)
    if file_extention != '.txt':
        raise NotImplementedError('Only .txt files are available')
    with open(file, 'r') as f:
        file_string = f.read()
    return file_string


def store_file_content(content, file='new_file.txt'):
    with open(file, 'w') as f:
        f.write(content)
    return file

def get_file_extention(file: str):
    if file.startswith('.'):
        dot = file.find('.', 1)
    dot = file.find('.')
    if dot < 0:
        raise ValueError('extention not found')
    return file[dot:]
