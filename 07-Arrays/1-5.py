arr = [1, 2, 3, 4, 5]
index = len(arr)
print(arr)

arr[0] = arr[0] -1
print(arr)

index = index + 4
print(arr)

middle_index = len(arr) // 2
arr[middle_index] *= 2

print(arr)