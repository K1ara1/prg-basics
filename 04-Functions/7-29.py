def factorial(n):

    if n==0 or n==1:
        return 1

    if n > 1:
        return n * factorial(n-1)
    
result = int(input('Enter number: '))
print(factorial(result))