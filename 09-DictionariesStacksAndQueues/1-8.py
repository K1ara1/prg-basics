price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
count = 0
for key, value in price_list.items():
    print(key, value)
for value in price_list.values():
    count += value
print(count)

updated = {}
count = 0
for key, value in price_list.items():
    new_value = value*0.9
    updated[key] = new_value
    count += new_value
    print(key,new_value)
print(count)