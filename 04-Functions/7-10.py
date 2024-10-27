def f(x, y):

    count = 0
    for num in range(x, y):
        if num < 0 and num % 2 == 0:
            count += 1
    return count

numberx = int(input('Enter number x: '))
numbery = int(input('Enter number y: '))

print(f'f({numberx},{numbery}) returns {f(numberx, numbery)}')