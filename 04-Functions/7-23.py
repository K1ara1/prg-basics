def f(password):
    
    if len(password) < 6:
        return False
    return len(password) == len(set(password))
    

result = input('Enter password: ')
print(f(result))

