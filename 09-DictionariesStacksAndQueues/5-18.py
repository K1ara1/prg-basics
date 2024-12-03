import json

with open('dogs.json') as file:
    content = json.load(file)

for dog in content:
    if int(dog['age']) < 5:
        print(dog)