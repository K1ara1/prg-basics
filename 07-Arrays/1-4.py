arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[len(arr) -1])
print(arr[0] + arr[-1])
print(arr[int(len(arr)/2)])

for i in range(len(arr)):
    arr[i] = arr[i] -1
    print(arr[i], end = ' ')

for element in arr:
    print(element, end = ' ')
    



