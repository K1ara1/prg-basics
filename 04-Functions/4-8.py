def time_string(hours, minutes, time_format):
    hours = int(hours) 
    minutes = int(minutes)  

    if time_format == '24':
        return f'{hours:02}:{minutes:02}'  
    
    elif time_format == '12':
        if hours == 0:  
            return f'12:{minutes:02}'
        elif hours < 12:  
            return f'{hours}:{minutes:02}'
        elif hours == 12:  
            return f'12:{minutes:02}'
        else: 
            return f'{hours - 12}:{minutes:02}'

hours = input('Enter hours: ')
minutes = input('Enter minutes: ')
time_format = input('Enter format: ')

time = time_string(hours, minutes, time_format)
print(f'The formatted time is: {time}')


