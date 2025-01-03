filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

def tolerance_check(tolerance_percentage):
    lower_limit = 500 - (500 * tolerance_percentage)
    upper_limit = 500 + (500 * tolerance_percentage)
    return lambda x: x < lower_limit or x > upper_limit

check_tolerance = tolerance_check(0.02)  

incorrectly_filled = list(filter(check_tolerance, filled_bottles))

incorrect_percentage = (len(incorrectly_filled) / len(filled_bottles)) * 100

print(f"Bottle capacity:    500ml")
print(f"Filling tolerance:  2%")
print(f"Filled bottles:     {', '.join(map(str, filled_bottles))}")
print(f"Incorrectly filled: {int(incorrect_percentage)}%")