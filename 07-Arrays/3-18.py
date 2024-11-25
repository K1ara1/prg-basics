class MyArrays:
    def second_largest(array):
        # Find the second largest element without using built-in functions
        largest = second = float('-inf')
        for num in array:
            if num > largest:
                second = largest
                largest = num
            elif num > second and num != largest:
                second = num
        return second

    def range_difference(array):
        # Find the difference between the largest and smallest elements
        largest = smallest = array[0]
        for num in array:
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num
        return largest - smallest

    def median(array):
        # Find the median of the array
        # Sort the array manually
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
        n = len(array)
        if n % 2 == 1:
            return array[n // 2]
        else:
            return (array[n // 2 - 1] + array[n // 2]) / 2

    def min_max(array):
        # Return a two-element array containing the smallest and largest values
        largest = smallest = array[0]
        for num in array:
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num
        return [smallest, largest]

    def array_to_string(array):
        result = ""
        for i in range(len(array)):
            result += str(array[i])
            if i != len(array) - 1:
                result += " "
        return result

numbers = [7, 3, 8, 5, 2]

# Using the MyArrays module
second_largest = MyArrays.second_largest(numbers)
range_diff = MyArrays.range_difference(numbers)
median_value = MyArrays.median(numbers)
min_max_values = MyArrays.min_max(numbers)
numbers_as_string = MyArrays.array_to_string(numbers)

print("Numbers:", MyArrays.array_to_string(numbers)) 
print("Second largest number:", second_largest)
print("Range (Largest - Smallest):", range_diff)
print("Median:", median_value)
print("Smallest and largest number:", MyArrays.array_to_string(min_max_values))
print("Numbers as a string:", numbers_as_string)