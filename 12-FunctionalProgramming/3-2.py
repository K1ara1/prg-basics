sentence = 'I completely agree with you'
result = list(map(lambda number: len(number), sentence.split()))
print(result)