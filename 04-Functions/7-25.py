def f(x,y):
    counter = 0
    for number in range(x,y + 1):
        if number%2 == 0 and number%3 == 0 and number%4 != 0:
            counter += number
    return counter

first = int(input('Enter x: '))
last = int(input('Enter y: '))
print(f(first, last))
