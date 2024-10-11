import math
tree_circumference = int(input('Tree circumference: '))
tree_ok = tree_circumference/math.pi >= 50
print(f'Tree can be cut: {tree_ok}')