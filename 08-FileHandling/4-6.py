import re

filename = input('Enter filename: ')

try:
    with open(filename, 'r') as file:
        content = file.read()

    lines_pattern = '.+'
    characters_pattern = '\S'
    words_pattern = '\w+'

    lines = re.findall(lines_pattern, content)
    len_lines = len(lines)

    characters = re.findall(characters_pattern, content)
    count = 0
    len_char = len(characters)

    words = re.findall(words_pattern, content)
    len_words = len(words)

    print('File name:', filename)
    print('Number of lines:', len_lines)
    print('Number of characters:', len_char)
    print('Number of words:', len_words)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")