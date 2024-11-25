import random

def rand_elem(array):
    return random.choice(array)


array=[10,20,30,40,50,60]

print([rand_elem(array),rand_elem(array),rand_elem(array)])