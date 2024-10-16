light_switch1 = False 
light_switch2 = False
bulbs_on = 0

question1 = input('Do you want to turn on first switch: (Y/N):')
if question1 == 'Y':
    light_switch1 = True
    bulbs_on += 1
question2 = input('Do you want to turn on second switch: (Y/N):')
if question2 == 'Y':
    light_switch2 = True
    bulbs_on += 2
print(f'{bulbs_on} bulbs are lit')