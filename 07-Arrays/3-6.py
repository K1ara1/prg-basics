array = [15, 8, 31, 47, 2, 19]

count = 0
i = 0

while i < len(array):
    count += array[i]
    i += 1 

mean = count/len(array)

print(mean)