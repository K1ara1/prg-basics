def f(amount_to_pay):
    
    coins = [5, 2, 1]
    coin_count = 0

    for coin in coins:
        coin_count += amount_to_pay // coin
        amount_to_pay %= coin

    return coin_count

machine = int(input('Enter price you have to pay: '))
result = f(machine)

print(f'{machine} returns {result}')
