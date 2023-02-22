# file_reader.py

def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        word_count = len(text.split())
    return word_count