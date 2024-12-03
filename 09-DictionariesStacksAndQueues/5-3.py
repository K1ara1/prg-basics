translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

word = input('Enter your word: ')
for key,value in translations.items():
    if word == key:
        print(value)
        break
else:
    print('translation is unavailable')