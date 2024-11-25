array = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest = array[0]

for name in array:
    if len(name) > len(longest):
        longest = name
print(longest)
