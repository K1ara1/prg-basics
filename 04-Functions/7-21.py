def f(number1,number2,number3):

    numbers = [number1, number2, number3]
    difference = max(numbers) - min(numbers)

    return difference

x = int(input('Enter number 1: '))
y = int(input('Enter number 2: '))
z = int(input('Enter number 3: '))

print(f(x, y, z))
