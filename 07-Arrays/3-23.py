def count_words(text):
    words = text.split()
    return len(words)

def words_by_length(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)

def words_alphabetically(text):
    words = text.split()
    return sorted(words)

text = "An apple a day keeps the doctor away"

word_count = count_words(text)
longest_to_shortest = words_by_length(text)
alphabetical_order = words_alphabetically(text)

print("Text:", text)
print("Number of words:", word_count)

print("Words from the longest:")
for word in longest_to_shortest:
    print(word)

print("Words ordered alphabetically:")
for word in alphabetical_order:
    print(word)