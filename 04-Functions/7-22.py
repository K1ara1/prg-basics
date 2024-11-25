def f(name):

    words = name.split()
    acronym = ""
    
    for word in words:
        acronym += word[0]
    return acronym

result = input('Enter text: ')
print(f(result))