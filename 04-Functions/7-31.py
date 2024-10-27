def power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * power(x, n - 1)
    else:
        return 1 / power(x, -n)
    
result1 = int(input('Enter x: '))
result2 = int(input('Enter n: '))
print(power(result1,result2))