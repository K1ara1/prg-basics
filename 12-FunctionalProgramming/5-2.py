from functools import reduce
numbers = [2,4,6,3,7,5]
even_numbers = filter(lambda num: num%2 ==0,numbers)
sum_of_evens = reduce(lambda x, y: x + y, even_numbers)
print(sum_of_evens)