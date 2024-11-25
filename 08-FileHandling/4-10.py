import csv

file_name = 'clothing.csv'

with open(file_name, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row['Price'])
        stock_quantity = int(row['Stock_Quantity'])
        if price < 60 and stock_quantity < 40:
            print(row['Product_ID'],row['Product_Name'])
