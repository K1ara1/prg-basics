def f(number):
    
    str_num = str(number)
    digit_count = {}
    
    for digit in str_num:
        if digit.isdigit():  
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1
    
    total_sum = 0
    for digit, count in digit_count.items():
        if count > 1:  
            total_sum += int(digit) * count  
    
    return total_sum

result = input('Enter number: ')
print(f(result))