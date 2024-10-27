import letters

text = input('Enter text: ')
letter = input('Enter letter to count: ')

count = letters.letter_calculations(text, letter)

print(f'The number of letter {letter}: {count} ')