import re

files = 'files.txt'

with open(files) as file:
    content = file.read()

pattern = '^[\\w\\-.]+(?:\\.[a-zA-Z0-9]{4})$'

matching_files = re.findall(pattern, content, re.MULTILINE)

for filename in matching_files:
    print(filename)