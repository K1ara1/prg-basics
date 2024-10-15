month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month < 10 <= 7:
    quater = 3
elif month < 7 :
    quater = 2
elif month < 4:
    quater = 1
else:
    print("Wrong number")

print(f'Month {month} is in quarter {quater}')