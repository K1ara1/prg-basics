import json

filename = 'votes.json'

try:
    with open(filename, 'r') as file:
        votes = json.load(file) 
except FileNotFoundError:
    votes = {}  

person_name = input('Name of the person you are voting for: ')

if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1 

with open(filename, 'w') as file:
    json.dump(votes, file, indent=4)

print(f"Updated votes: {votes}")