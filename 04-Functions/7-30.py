def sum_natural(n):
    if n < 1:
        return 'Only natural numbers!'
    if n == 1:
        return 1
    if n > 1:
        return n + sum_natural(n - 1)

result = int(input('Enter number: '))
print(sum_natural(result))