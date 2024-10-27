def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    digit = (int(product_code[0]) + int(product_code[1]) + int(product_code[2]))%7

    return digit == int(product_code[3])

result = input('Enter 4 digit number: ')
print(f(result))