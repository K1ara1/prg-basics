first = input('Enter first letter: ')
last = input('Enter last letter: ')
if first == last:
    letters_between = 0
else:
    letters_between = abs(ord(first) - ord(last)) - 1
print(f'Between {first} and {last} is {letters_between} letters')