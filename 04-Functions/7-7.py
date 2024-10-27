def f(binary_number):

    for char in binary_number:
        if char != '0' and char != '1':
            return False 
    return True

bin = input('Enter number to check if it is binary: ')
result = f(bin)

print(f"f('{bin}') returns {result}")