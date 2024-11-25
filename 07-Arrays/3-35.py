def transpose_matrix(m):

    transposed = []
    
    for j in range(len(m[0])):  # m[0] is the first row (number of columns)
        row = []  # Create an empty list for each new row in the transposed matrix
        for i in range(len(m)):  # Iterate over the rows of the original matrix
            row.append(m[i][j])  # Append the element to the new row
        transposed.append(row)  # Add the new row to the transposed matrix
    
    return transposed

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")  
        print()  

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [5, 6, 7, 8, 0]
]

print("Original matrix 1:")
print_matrix(matrix1)
print("\nTransposed matrix 1:")
transposed1 = transpose_matrix(matrix1)
print_matrix(transposed1)

print("\nOriginal matrix 2:")
print_matrix(matrix2)
print("\nTransposed matrix 2:")
transposed2 = transpose_matrix(matrix2)
print_matrix(transposed2)