def f(number1,number2,operator):
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '%':
        result = number1 % number2
    elif operator == '**':
        result = number1 ** number2
    else:
        return 'Invalid operator'
    return result

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
op = input('Enter operator: ')

print(f(x, y, op))
    