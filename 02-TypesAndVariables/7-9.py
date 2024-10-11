import random
dice_roll = random.randint(1,6)
special_dice_roll = dice_roll == 1 or dice_roll == 6
print(f'Dice rolled: {dice_roll}')
print(f'Special number: {special_dice_roll}')