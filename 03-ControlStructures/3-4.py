x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 or not y < 0 :
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print(f'None of the numbers {x} and {y} is not negative')