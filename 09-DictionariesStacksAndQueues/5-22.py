import json

product = {}
product["name"] = input("Enter the product name: ")
product["price"] = float(input("Enter the product price (e.g., 12.34): "))
paid_input = input("Has the product been paid for? (yes/no): ")
if paid_input in ['yes', 'y']:
    product["paid"] = True
elif paid_input in ['no', 'n']:
    product["paid"] = False
else:
    print("Invalid input for 'paid'. Defaulting to 'False'.")
    product["paid"] = False

with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, indent=4, ensure_ascii=False)
print("Product data saved to 'product.json'.")

