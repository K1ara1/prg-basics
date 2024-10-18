time = input('Enter time (24-hour format): ')

if int(time[:2]) > 12:
    time_change = (int(time[:2]) - 12) 
print(f"Time in 12-hour format is {time_change}:{time[3:6]}")
