age = int(input('Enter your age: '))

if 0 < age < 13:
    print('You are a child')
elif 20 > age > 12:
    print('You are a teen')
elif 65 > age > 19:
    print('You are an adult')
elif age >= 65:
    print('You are a senior')
else:
    print('You are not born yet')