import os

DICTIONARY = {
    'doc': 'texts',
    'txt': 'texts',
    'jpg': 'pictures',
    ''
}

def sort_files(directory):
    for f in os.listdir(directory):
        extension = f.split('.')[-1]
        if extension not in DICTIONARY:
            continue
        new_directory = f'{directory}/{DICTIONARY[extension]}'
        if not os.path.exists(new_directory) or not os.path.isdir(new_directory):
            os.mkdir(new_directory)
        os.rename(f'{directory}/{f}')
        f'{new_directory}/{f}')