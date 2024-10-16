dog_age = int(input('Enter dog`s age in human years: '))

if dog_age < 0:
    print('Age must be a positive number')
    exit()
elif dog_age <= 2:
    dog_years = dog_age*10.5
else:
    dog_years = 21 + (dog_age - 2) * 4
print(f"The dog`s age in dog`s years is {dog_years}")