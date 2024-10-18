products = int(input('Enter the number of products purchased: '))
price = int(input('Enter product price in PLN: '))

if products == 1 or products == 2:
    amount = price*products
elif products >= 3:
    amount = (products - 2)*price*0.75
    print(f'Number of products purchased is {products}')
    print(f'Product price is {price} PLN')
    print(f'Amount to pay is {amount} PLN')
