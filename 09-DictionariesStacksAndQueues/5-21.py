import json

sth = {
    'ab': {
    'fun' : 'fun',
    'crazy':'fun:',
    'marvelous':'fun'}
}
with open('favourite.json', 'w') as file:
    json.dump(sth,file, indent = 4)


print("Data saved to 'favourite.json'.")