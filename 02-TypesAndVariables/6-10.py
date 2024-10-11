movie = "The Lord of the Rings: The Return of the King"

print(f'Number of characters: {len(movie)}')
print ('Title in capital letters: ', movie.title())
print ('Title in small letters: ', movie.casefold())
print ('How many times the vowel "e" appears in the title: ', movie.count('e'))
print ('Where in the text is the word "Lord": ', movie.index('Lord'))
print ('Where in the text is the word "dragon": ', movie.find('dragon'))

