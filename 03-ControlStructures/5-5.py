total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    total_sum += number
    count += 1
    
    if number == 0:
        break 
if count > 0:
    arithmetic_mean = total_sum / count
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The arithmetic mean of the numbers is: {arithmetic_mean:.2f}")
else:
    print("No numbers were entered.")