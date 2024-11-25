array = [
    [-38, 19], 
    [5,40],
    [-7,11],
    [29,16]
]

min_value = float('inf')  # Smallest value starts as infinity
max_value = float('-inf')  # Largest value starts as negative infinity
min_position = (-1, -1)  # Placeholder for the row and column of the smallest value
max_position = (-1, -1)  # Placeholder for the row and column of the largest value

# Loop through the array to find the smallest and largest values
for i in range(len(array)):  # Loop through rows
    for j in range(len(array[i])):  # Loop through columns
        if array[i][j] < min_value:  # Check for the smallest value
            min_value = array[i][j]
            min_position = (i, j)  # Update the position of the smallest value
        if array[i][j] > max_value:  # Check for the largest value
            max_value = array[i][j]
            max_position = (i, j)  # Update the position of the largest value

# Print the results
print("Smallest value:", min_value, "at row", min_position[0], "column", min_position[1])
print("Largest value:", max_value, "at row", max_position[0], "column", max_position[1])