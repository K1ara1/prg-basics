array = [
    [1, 2, 3, 4, 5],  # First row
    [6, 7, 8, 9, 10],  # Second row
    [11, 12, 13, 14, 15]  # Last row
]

# Function to print the 2D array in rows and columns
def print_array(arr):
    for row in arr:
        for value in row:
            print(value, end=" ")  # Print values in a row separated by space
        print()  # Newline after each row

print("Array before swapping:")
print_array(array)

# Swap the first and last rows
array[0], array[-1] = array[-1], array[0]

print("\nArray after swapping:")
print_array(array)