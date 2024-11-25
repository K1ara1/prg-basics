array = [15, 38, 7, 23, 14]
num = int(input('Enter your number: '))
def occurs(number, array):
    for i in array:
        if i == number:
            return True
if occurs(num, array):
    print(f'Result: {num} appears in the array')
else:
    print(f'Result: {num} does not appear in the array')
        