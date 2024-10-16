hours = int(input("Enter the number of hours the car was parked: "))

if hours == 1 or hours == 2:
    print("You have to pay 5 PLN")
elif 7 > hours > 2:
    print("You have to pay 15 PLN")
elif hours > 6:
    print("You have to pay 20 PLN")
else:
    print("Enter correct number of hours")