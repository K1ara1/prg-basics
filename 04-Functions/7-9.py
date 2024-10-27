def f(number, even):

    digit_sum = 0
    
    for digit in str(number):
        digit = int(digit)
        if (even and digit % 2 == 0) or (not even and digit % 2 != 0):
            digit_sum += digit
    
    return digit_sum

num = input('Enter your number: ')
result = f(num)

print(result)