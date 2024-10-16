current = float(input('Enter current product price: '))
previous = float(input('Enter previous product price: '))

difference = 100 - current/previous*100

if difference >= 10:
    print(f'Current product price: {current}')
    print(f'Previous product price: {previous}')
    print('Buy the product!')
    print(f'Product price reduced by {difference}%')
    