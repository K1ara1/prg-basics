month = int(input('Enter month number (1..12): '))

if month >= 10:
    quater = 4
elif 10 > month >= 7:
    quater = 3
elif 7 > month >= 4:
    quater = 2
elif 4 > month >= 1:
    quater = 1
else:
    print("Wrong number")

print(f'Month {month} is in quarter {quater}')