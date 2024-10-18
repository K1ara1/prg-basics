car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if speed_limit_max < car_speed or speed_limit_min > car_speed:
    print('Warning: invalid car speed!!')