arr = [7,9,2,4,5,6]

storage_even = []
storage_odds = []

for num in arr:
    if num %2 == 0:
        storage_even.append(num)
    else:
        storage_odds.append(num)

print(storage_even + storage_odds)
