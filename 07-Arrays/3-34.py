def identity_matrix(n):
    # Create an empty list (matrix)
    matrix = []
    
    # Loop through rows (n rows)
    for i in range(n):
        row = []  # Create an empty row
        
        # Loop through columns (n columns)
        for j in range(n):
            if i == j:  # If it's the diagonal (row == column), put 1
                row.append(1)
            else:  # Otherwise, put 0
                row.append(0)
        
        # Add the row to the matrix
        matrix.append(row)
    
    return matrix

# Function to print the matrix in a readable format
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")  # Print each number in a row with a space
        print()  # After printing each row, move to the next line

# Main program to create and print identity matrices of sizes 3, 5, and 8
print("Identity matrix of size 3:")
matrix_3 = identity_matrix(3)  # Create a 3x3 identity matrix
print_matrix(matrix_3)  # Print the 3x3 matrix

print("\nIdentity matrix of size 5:")
matrix_5 = identity_matrix(5)  # Create a 5x5 identity matrix
print_matrix(matrix_5)  # Print the 5x5 matrix

print("\nIdentity matrix of size 8:")
matrix_8 = identity_matrix(8)  # Create an 8x8 identity matrix
print_matrix(matrix_8) 