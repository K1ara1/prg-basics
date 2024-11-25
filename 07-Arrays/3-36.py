def convert_to_1d(array):
    
    one_dimensional_array = []

    for row in array:
        for element in row:
            one_dimensional_array.append(element)
    return one_dimensional_array

array1 = [
    [2, 3],
    [1, 5]
]

array2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

array3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

print("1D array from array1:")
print(convert_to_1d(array1))

print("\n1D array from array2:")
print(convert_to_1d(array2))

print("\n1D array from array3:")
print(convert_to_1d(array3))