total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

if program == 'j':
    total_washing_time += 40
    if extra_rinse == 'y':
        total_washing_time += 15
    if extra_spin == 'y':
        total_washing_time += 9
elif program == 'u':
    total_washing_time += 70
    if extra_rinse == 'y':
        total_washing_time += 15
    if extra_spin == 'y':
        total_washing_time += 9
elif program == 's':
    total_washing_time += 20
    if extra_rinse == 'y':
        total_washing_time += 15
    if extra_spin == 'y':
        total_washing_time += 9
else:
    print('Wrong program')

print(f'Total washing time is {total_washing_time}')
