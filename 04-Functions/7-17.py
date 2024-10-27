def f(palindrome):
    normalized_list = []
    
    for char in palindrome:
        normalized_list.append(char.lower()) 
    
    return normalized_list == normalized_list[::-1]

word = input('Enter word: ')
print(f(word))