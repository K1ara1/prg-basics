def create_2d_arr(x,y):
    array = []
    
    for i in range(x):
        row = []  # Start with an empty row
        for j in range(y):
            row.append(0)  # Add 0 to the row
        array.append(x)  # Add the row to the array
    return array

rows = 3
cols = 5
array_3x5 = create_2d_arr(rows, cols)

print("Created 2D array:")
for item in array_3x5:
    print(item)