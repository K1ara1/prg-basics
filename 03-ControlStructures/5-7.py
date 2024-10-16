import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 5:
    print(countdown)
    countdown -= 1
    time.sleep(1) 
if countdown == 5:
    print('five')
    countdown -= 1
    time.sleep(1)
if countdown == 4:
    print('four')
    countdown -= 1
    time.sleep(1)
if countdown == 3:
    print('three')
    countdown -= 1
    time.sleep(1)
if countdown == 2:
    print('two')
    countdown -= 1
    time.sleep(1)
if countdown == 1:
    print('one')
    countdown -= 1
    time.sleep(1)


print("Time's up!")


















