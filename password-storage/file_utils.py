def get_file_content(file):
    with open(file, 'r') as f:
        file_string = f.read()
    return file_string
