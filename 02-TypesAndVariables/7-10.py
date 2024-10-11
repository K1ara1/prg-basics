import random
computer = random.randint(1,6)
you = int(input('Enter number from the dice: '))
correct = computer == you
print(f'You won: {correct}')