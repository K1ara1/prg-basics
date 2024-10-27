def f(name):

    words = name.split()
    acronym = ""
    
    for word in words:
        if word: 
            acronym += word[0].upper()
    return acronym

result = input('Enter text: ')
print(f(result))