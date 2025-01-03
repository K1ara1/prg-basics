names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

sorting = lambda name: sorted(name, key=len)

result = sorting(names)
print(result)