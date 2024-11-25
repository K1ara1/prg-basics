def is_subset(arr1, arr2):
    for element in arr1:
        if element not in arr2:
            return False
    return True

arr1 = [1, 2, 3]
arr2 = [3, 2, 1, 4, 5]

if is_subset(arr1, arr2):
    print("The first array is a subset of the second array.")
else:
    print("The first array is NOT a subset of the second array.")