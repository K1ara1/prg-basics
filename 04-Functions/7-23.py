def f(password):
    
    if len(password) < 6 or len(password) != len(set(password)):
        return False
    else:
        return True

    

result = input('Enter password: ')
print(f(result))

