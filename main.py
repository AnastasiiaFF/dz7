
from pathlib import Path
from fill_numbers import generate_number_file
from group_rename import group_rename
from generate_names import generate_name_file
from process_file import process_files
from process_file import read_line_or_begin
from make_files import generate_text
from make_files import generate_files
from sort_files import sort_files


if __name__ == '__main__':
    generate_number_file(10, 'data.txt')

    process_files('data.txt', 'data_names.txt', 'res.txt')

    generate_name_file('data_names.txt', 25)

    generate_files('rnd', 'files')

    sort_files('files')

    group_rename(4, 'bin', 'zip', [2, 4], "new_file")