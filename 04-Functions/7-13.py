def f(n):
    result = ''
    for i in range(1,n + 1):
        result += str(i)
    return result
number = int(input('Enter number: '))
print(f(number))