price_string = input("Enter price: ")
discount_string = input("Enter discount: ")
price = float(price_string)
discount = int(discount_string)
price_with_discount = price*(100-discount)/100
reduction = price - price_with_discount
print(f"The product price is {price}.")
print(f"The discount is {discount}%.")
print(f"The product price with discount is {price_with_discount:.2f}.")
print(f"The difference between the product price before and after the discount is {reduction:.2f}.")