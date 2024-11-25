filename = 'powers.txt'

with open(filename, 'w') as file:
    for i in range(1, 101):
        second_power = i**2
        third_power = i**3
        line = f"{i},{second_power},{third_power}\n"
        file.write(line)