amount = int(input('Enter the amount in PLN: '))
coins = [5, 2, 1]

if amount > 0:
    coin_count = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            coin_count[coin] = count
            amount -= coin * count
    print("Coins used to make the amount:")
    for coin, count in coin_count.items():
        print(f"{coin}PLN: {count}")
else:
    print("Please enter a natural number.")