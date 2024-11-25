arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

for row in arr:
    for item in row:
        sum = arr[0][4] + arr[1][4] + arr[2][4] + arr[3][4]
print(sum)