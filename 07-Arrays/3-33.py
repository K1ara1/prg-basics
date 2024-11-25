array = [
    [1, 2, 3, 4, 5],  # First row
    [6, 7, 8, 9, 10],  # Second row
    [11, 12, 13, 14, 15]  # Third row
]

# Function to print the 2D array in rows and columns
def print_array(arr):
    for row in arr:
        for value in row:
            print(value, end=" ")  # Print values in a row separated by space
        print()  # Newline after each row

print("Array before swapping:")
print_array(array)

for row in array:
    row[0], row[-1] = row[-1], row[0] 

print("\nArray after swapping:")
print_array(array)