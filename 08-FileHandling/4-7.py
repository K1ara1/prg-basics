import re
text = input('Enter text: ')

pattern = '[aeiouAEIOU]'

vowels = re.findall(pattern, text)

print(len(vowels))

