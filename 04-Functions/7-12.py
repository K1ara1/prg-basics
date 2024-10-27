def f(n: int) -> str:
    
    result = ''
    
    for i in range(n):
        result += '*' 
        if i < n - 1:
            result += '/' 
            
    return result

number = int(input('Enter number: '))
print(f(number))
        