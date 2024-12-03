def bubblesort(array):
    
    for i in range(len(array)):
        for j in range(len(array)- i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
    return array

arr1=[2,4,5,1,2,7]
print(bubblesort(arr1))