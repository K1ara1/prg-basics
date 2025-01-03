avg_speed = lambda d,h,m: d/(h + m/60)

distance = int(input('Enter distance in km: '))
hours = int(input('Enter number of travel hours: '))
minutes = int(input('Enter number of travel minutes: '))

avg = avg_speed(distance,hours,minutes)
print(f'Average speed: {round(avg,1)}')