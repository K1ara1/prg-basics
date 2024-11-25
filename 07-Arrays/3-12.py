def print_unique_elements(array):
    element_count = {}

    for num in array:
        if num in element_count:
            element_count[num] += 1  
        else:
            element_count[num] = 1  

    unique_elements = []
    for num, count in element_count.items():
        if count == 1:
            unique_elements.append(num)
    print("Unique elements:", unique_elements)

array = [2, 3, 2, 5, 8, 1, 9, 8]
print_unique_elements(array)