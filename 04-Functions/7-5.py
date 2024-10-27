import range

x = int(input('Enter x: '))
y = int(input('Enter y: '))
number = int(input('Enter number: '))

result = range.is_in_range(number, x, y)

if result:
    print(f"The number {number} is within the range ({x}, {y}).")
else:
    print(f"The number {number} is NOT within the range ({x}, {y}).")
