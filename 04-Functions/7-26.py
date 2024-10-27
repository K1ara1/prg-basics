def f(text):
    new = ""
    
    for i in range(len(text)):
        new += text[i]  
        if i < len(text) - 1: 
            new += "-"
    
    return new
result = input('Enter text: ')
print(f(result))