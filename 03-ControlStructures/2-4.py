number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operator = input("Enter mathematical operation (+, -, *, /): ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1*number2
else:
    result = number1/number2
print(result)